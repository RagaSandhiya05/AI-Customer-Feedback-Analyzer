import streamlit as st
from transformers import pipeline
import pandas as pd


st.set_page_config(
    page_title="AI Customer Feedback Analyzer",
    page_icon="💬",
    layout="wide"
)


@st.cache_resource
def load_sentiment_pipeline():
    """Load the pretrained sentiment model once."""
    return pipeline("sentiment-analysis")


def analyze_reviews(texts):
    """Predict sentiment and confidence for multiple reviews."""
    nlp = load_sentiment_pipeline()

    # Limit each review's text length.
    cleaned_texts = [text[:1000] for text in texts]

    return nlp(cleaned_texts, truncation=True)


def display_sentiment(label):
    """Return a readable sentiment label."""
    label = str(label).upper()

    if label.startswith("POS"):
        return "Positive"
    elif label.startswith("NEG"):
        return "Negative"

    return label


def main():
    st.title("💬 AI Customer Feedback Analyzer")
    st.write(
        "Analyze customer feedback using a pretrained "
        "Hugging Face Transformer model."
    )

    single_tab, bulk_tab = st.tabs(
        ["Single Review", "Bulk CSV Analysis"]
    )

    # SINGLE REVIEW ANALYSIS
    with single_tab:
        st.subheader("Analyze an individual review")

        review = st.text_area(
            "Enter your customer review",
            height=160,
            placeholder=(
                "Example: The product quality is excellent "
                "and delivery was very fast!"
            )
        )

        if st.button(
            "Analyze Sentiment",
            type="primary",
            key="single_analyze"
        ):
            if not review.strip():
                st.warning("Please enter a customer review.")
            else:
                try:
                    with st.spinner("Analyzing your review..."):
                        result = analyze_reviews([review])[0]

                    label = result["label"]
                    confidence = result["score"]
                    sentiment = display_sentiment(label)

                    if sentiment == "Positive":
                        st.success("Sentiment: 😊 Positive")
                    elif sentiment == "Negative":
                        st.error("Sentiment: 😞 Negative")
                    else:
                        st.info(f"Sentiment: {sentiment}")

                    st.metric(
                        "Model confidence",
                        f"{confidence:.1%}"
                    )

                    st.progress(float(confidence))

                    st.caption(
                        "Confidence is the model's score, "
                        "not a guarantee that the prediction is correct."
                    )

                except Exception as e:
                    st.error(
                        f"Could not analyze the review: {e}"
                    )

    # BULK CSV ANALYSIS
    with bulk_tab:
        st.subheader("Analyze multiple customer reviews")

        st.write(
            "Upload a CSV file containing a column named "
            "`review`."
        )

        uploaded_file = st.file_uploader(
            "Choose a CSV file",
            type=["csv"]
        )

        if uploaded_file is not None:
            try:
                df = pd.read_csv(uploaded_file)

                # Ignore leading/trailing spaces in column names.
                df.columns = df.columns.str.strip()

                if "review" not in df.columns:
                    st.error(
                        "Your CSV must contain a 'review' column."
                    )
                else:
                    # Remove missing and empty reviews safely.
                    df["review"] = df["review"].fillna("").astype(str).str.strip()
                    df = df[df["review"] != ""].copy()

                    if df.empty:
                        st.warning(
                            "No non-empty reviews were found."
                        )
                    else:
                        with st.spinner(
                            "Analyzing customer feedback..."
                        ):
                            results = analyze_reviews(
                                df["review"].tolist()
                            )

                        df["sentiment"] = [
                            display_sentiment(r["label"])
                            for r in results
                        ]

                        df["confidence"] = [
                            round(float(r["score"]), 4)
                            for r in results
                        ]

                        # Summary metrics
                        total = len(df)
                        positive = int(
                            (df["sentiment"] == "Positive").sum()
                        )
                        negative = int(
                            (df["sentiment"] == "Negative").sum()
                        )

                        col1, col2, col3 = st.columns(3)

                        col1.metric("Total Reviews", total)
                        col2.metric("Positive Reviews", positive)
                        col3.metric("Negative Reviews", negative)

                        st.subheader("Sentiment Distribution")

                        sentiment_counts = (
                            df["sentiment"].value_counts()
                        )

                        st.bar_chart(sentiment_counts)

                        st.subheader("Detailed Results")
                        st.dataframe(
                            df,
                            use_container_width=True
                        )

                        csv_data = df.to_csv(
                            index=False
                        ).encode("utf-8")

                        st.download_button(
                            label="Download Results as CSV",
                            data=csv_data,
                            file_name="sentiment_results.csv",
                            mime="text/csv"
                        )

            except Exception as e:
                st.error(
                    f"Could not process the uploaded CSV: {e}"
                )


if __name__ == "__main__":
    main()
