---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "shared"
message_set: "T2S Administration"
source_ids: ["src-000344"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["5 Message Items Types", "5.1 MessageComponents", "5.1.7 Miscellaneous", "5.1.7.1 MessageHeader7", "5.1.7.1.4 OriginalBusinessQuery <OrgnlBizQry>"]
file_pages: [51]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 5.1.7.1.4 OriginalBusinessQuery <OrgnlBizQry>

Source: [src-000344](../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Administration_MessageSet/ISO20022_MDRPart2_Target2Securities_Administration_2023_2024_v1.pdf`. Locator: one-based file pages 51 to 51.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 51

```text
5.1.7.1.4  OriginalBusinessQuery <OrgnlBizQry>
Presence: [0..1]
Definition: Unique identification of the original query message.
OriginalBusinessQuery <OrgnlBizQry> contains the following elements (see
"OriginalBusinessQuery1" on page 52 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 52
   MessageNameIdentification <MsgNmId> [0..1] Text 53
   CreationDateTime <CreDtTm> [0..1] DateTime 53
5.1.7.1.5  QueryName <QryNm>
Presence: [0..1]
Definition: Recalls the criteria (search and return criteria) defined in a preceding query.
Datatype: "Max35Text" on page 69
5.1.7.2  SequenceRange1Choice
Definition: Specifies a choice of sequences.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromSequence <FrSeq> [1..1] Text 51
Or   ToSequence <ToSeq> [1..1] Text 51
Or   FromToSequence <FrToSeq> [1..*]  52
     FromSequence <FrSeq> [1..1] Text 52
     ToSequence <ToSeq> [1..1] Text 52
Or   EqualSequence <EQSeq> [1..*] Text 52
Or}   NotEqualSequence <NEQSeq> [1..*] Text 52
5.1.7.2.1  FromSequence <FrSeq>
Presence: [1..1]
Definition: Start sequence of the range.
Datatype: "Max35Text" on page 69
5.1.7.2.2  ToSequence <ToSeq>
Presence: [1..1]
Definition: End sequence of the range.
Datatype: "Max35Text" on page 69
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
Message Items Types
Target2-Securities - Administration - Maintenance 2023 -
2024
51 March 2024
```

