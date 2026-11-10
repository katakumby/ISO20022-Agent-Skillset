---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "shared"
message_set: "T2S Administration"
source_ids: ["src-000344"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["5 Message Items Types", "5.1 MessageComponents", "5.1.7 Miscellaneous", "5.1.7.2 SequenceRange1Choice", "5.1.7.2.3 FromToSequence <FrToSeq>"]
file_pages: [52]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 5.1.7.2.3 FromToSequence <FrToSeq>

Source: [src-000344](../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Administration_MessageSet/ISO20022_MDRPart2_Target2Securities_Administration_2023_2024_v1.pdf`. Locator: one-based file pages 52 to 52.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 52

```text
5.1.7.2.3  FromToSequence <FrToSeq>
Presence: [1..*]
Definition: Particular sequence range specified between a start sequence and an end sequence.
FromToSequence <FrToSeq> contains the following SequenceRange1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromSequence <FrSeq> [1..1] Text 52
   ToSequence <ToSeq> [1..1] Text 52
5.1.7.2.3.1  FromSequence <FrSeq>
Presence: [1..1]
Definition: Start sequence of the range.
Datatype: "Max35Text" on page 69
5.1.7.2.3.2  ToSequence <ToSeq>
Presence: [1..1]
Definition: End sequence of the range.
Datatype: "Max35Text" on page 69
5.1.7.2.4  EqualSequence <EQSeq>
Presence: [1..*]
Definition: Specified sequence to match.
Datatype: "Max35Text" on page 69
5.1.7.2.5  NotEqualSequence <NEQSeq>
Presence: [1..*]
Definition: Specified sequence to be excluded.
Datatype: "Max35Text" on page 69
5.1.7.3  OriginalBusinessQuery1
Definition: Unique identification, as assigned by the original requestor, to unambiguously identify the
business query message.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 52
   MessageNameIdentification <MsgNmId> [0..1] Text 53
   CreationDateTime <CreDtTm> [0..1] DateTime 53
5.1.7.3.1  MessageIdentification <MsgId>
Presence: [1..1]
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
Message Items Types
Target2-Securities - Administration - Maintenance 2023 -
2024
52 March 2024
```

