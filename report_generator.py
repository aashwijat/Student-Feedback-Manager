from datetime import datetime
from collections import Counter

def summarize_feedback_basic(feedbacks):
    """A very basic summarization of provided feedback."""
    word_counts = Counter()
    positive_indicators = ["good", "great", "like", "helpful", "enjoyed"]
    negative_indicators = ["bad", "poor", "dislike", "difficult", "boring"]
    positive_mentions_count = 0
    negative_mentions_count = 0
    topic_mentions = {}

    for feedback in feedbacks:
        feedback = feedback.lower()
        words = feedback.split()
        for word in words:
            word_counts[word] += 1
            if word in positive_indicators:
                positive_mentions_count += 1
            elif word in negative_indicators:
                negative_mentions_count += 1
            if feedback.startswith("topic:"):
                try:
                    topic = feedback.split(":")[1].split(".")[0].strip()
                    topic_mentions[topic] = topic_mentions.get(topic, 0) + 1
                except IndexError:
                    pass

    top_words = word_counts.most_common(10)
    top_topics = sorted(topic_mentions.items(), key=lambda item: item[1], reverse=True)[:5]

    return {
        "total_feedbacks": len(feedbacks),
        "positive_mentions": positive_mentions_count,
        "negative_mentions": negative_mentions_count,
        "top_words": top_words,
        "top_topics": top_topics
    }

def generate_feedback_report_basic(feedbacks, report_file="basic_feedback_report.txt"):
    """Summarizes provided feedback and saves a basic report to a text file."""
    summary = summarize_feedback_basic(feedbacks)

    with open(report_file, 'w') as f:
        f.write("--- Basic Feedback Report ---\n")
        f.write(f"Report Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Total Feedbacks: {summary['total_feedbacks']}\n\n")

        f.write(f"Total Positive Mentions (of keywords): {summary['positive_mentions']}\n")
        f.write(f"Total Negative Mentions (of keywords): {summary['negative_mentions']}\n\n")

        f.write("Top Mentioned Words:\n")
        for word, count in summary['top_words']:
            f.write(f"- {word}: {count}\n")
        f.write("\n")

        f.write("Top Discussed Topics:\n")
        for topic, count in summary['top_topics']:
            f.write(f"- {topic}: {count}\n")
        f.write("\n")

        f.write("\n--- Provided Feedbacks ---\n")
        for feedback in feedbacks:
            f.write(f"- {feedback}\n")

    print(f"Basic feedback report generated and saved to '{report_file}'")

if __name__ == "__main__":
    student_feedbacks = [
        "Topic: lectures. The lectures were good and very helpful.",
        "Topic: assignments. The assignments were too difficult and boring.",
        "I really like the instructor's teaching style.",
        "The course material was poor and unclear.",
        "Topic: grading. The grading seemed fair and helpful.",
        "Enjoyed the interactive sessions a lot.",
        "Dislike the length of the assignments.",
        "The material was great and easy to understand.",
        "The instructor was not very helpful.",
        "Topic: lectures. The lectures were boring at times."
    ]
    report_filename = "basic_student_feedback_report.txt"
    generate_feedback_report_basic(student_feedbacks, report_filename)
