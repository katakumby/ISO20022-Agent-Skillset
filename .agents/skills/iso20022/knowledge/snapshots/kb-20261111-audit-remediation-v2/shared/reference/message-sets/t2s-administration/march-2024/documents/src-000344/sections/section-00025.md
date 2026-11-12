---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "shared"
message_set: "T2S Administration"
source_ids: ["src-000344"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["3 admi.006.001.01 ResendRequestV01", "3.4 Message Building Blocks", "3.4.2 ResendSearchCriteria <RsndSchCrit>", "3.4.2.4 OriginalMessageNameIdentification <OrgnlMsgNmId>"]
file_pages: [30, 31]
content_origin: "source-text-extraction"
mentioned_message_ids: ["admi.006.001.01"]
---

# 3.4.2.4 OriginalMessageNameIdentification <OrgnlMsgNmId>

Source: [src-000344](../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Administration_MessageSet/ISO20022_MDRPart2_Target2Securities_Administration_2023_2024_v1.pdf`. Locator: one-based file pages 30 to 31.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 30

```text
SequenceRange <SeqRg> contains one of the following elements (see "SequenceRange1Choice" on
page 51 for details)
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
3.4.2.4  OriginalMessageNameIdentification <OrgnlMsgNmId>
Presence: [0..1]
Definition: Unambiguously identifies the original bsiness message, which was delivered by the business
sender.
Datatype: "Max35Text" on page 69
3.4.2.5  FileReference <FileRef>
Presence: [0..1]
Definition: String of characters that uniquely identifies the file, which was delivered by the sender.
Datatype: "Max35Text" on page 69
3.4.2.6  Recipient <Rcpt>
Presence: [1..1]
Definition: Unique identification to unambiguously identify the recipient of the report message.
Recipient <Rcpt> contains the following elements (see "PartyIdentification136" on page 54 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 54
   LEI <LEI> [0..1] IdentifierSet 54
3.4.3 SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C3 "SupplementaryDataRule"
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
admi.006.001.01 ResendRequestV01
Target2-Securities - Administration - Maintenance 2023 -
2024
30 March 2024
```

## File page 31

```text
SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on
page 53 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 53
   Envelope <Envlp> [1..1] (External Schema) 53
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
admi.006.001.01 ResendRequestV01
Target2-Securities - Administration - Maintenance 2023 -
2024
31 March 2024
```

