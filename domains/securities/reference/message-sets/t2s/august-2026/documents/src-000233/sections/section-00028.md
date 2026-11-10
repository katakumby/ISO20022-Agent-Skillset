---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["3 admi.006.001.01 ResendRequestV01", "3.4 Message Building Blocks", "3.4.2 ResendSearchCriteria <RsndSchCrit>", "3.4.2.4 OriginalMessageNameIdentification <OrgnlMsgNmId>"]
file_pages: [60, 61]
content_origin: "source-text-extraction"
mentioned_message_ids: ["admi.006.001.01"]
---

# 3.4.2.4 OriginalMessageNameIdentification <OrgnlMsgNmId>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 60 to 61.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 60

```text
SequenceRange <SeqRg> contains one of the following elements (see "SequenceRange1Choice" on
page 2978 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromSequence <FrSeq> [1..1] Text 2978
Or   ToSequence <ToSeq> [1..1] Text 2978
Or   FromToSequence <FrToSeq> [1..*]  2978
     FromSequence <FrSeq> [1..1] Text 2978
     ToSequence <ToSeq> [1..1] Text 2978
Or   EqualSequence <EQSeq> [1..*] Text 2979
Or}   NotEqualSequence <NEQSeq> [1..*] Text 2979
3.4.2.4  OriginalMessageNameIdentification <OrgnlMsgNmId>
Presence: [0..1]
Definition: Unambiguously identifies the original bsiness message, which was delivered by the business
sender.
Datatype: "Max35Text" on page 3328
3.4.2.5  FileReference <FileRef>
Presence: [0..1]
Definition: String of characters that uniquely identifies the file, which was delivered by the sender.
Datatype: "Max35Text" on page 3328
3.4.2.6  Recipient <Rcpt>
Presence: [1..1]
Definition: Unique identification to unambiguously identify the recipient of the report message.
Recipient <Rcpt> contains the following elements (see "PartyIdentification136" on page 3060 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 3060
   LEI <LEI> [0..1] IdentifierSet 3060
3.4.3 SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C3 "SupplementaryDataRule"
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
admi.006.001.01 ResendRequestV01
Target2-Securities 60 August 2026
```

## File page 61

```text
SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on
page 3011 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 3011
   Envelope <Envlp> [1..1] (External Schema) 3012
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
admi.006.001.01 ResendRequestV01
Target2-Securities 61 August 2026
```

