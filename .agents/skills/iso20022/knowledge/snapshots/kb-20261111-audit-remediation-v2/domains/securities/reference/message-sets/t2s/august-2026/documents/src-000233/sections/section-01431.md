---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["33 reda.013.001.01 SecurityDeletionRequestV01", "33.4 Message Building Blocks", "33.4.2 FinancialInstrumentIdentification <FinInstrmId>"]
file_pages: [2041]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.013.001.01"]
---

# 33.4.2 FinancialInstrumentIdentification <FinInstrmId>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2041 to 2041.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2041

```text
MessageHeader <MsgHdr> contains the following elements (see "MessageHeader1" on page 2982 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 2982
   CreationDateTime <CreDtTm> [0..1] DateTime 2982
33.4.2 FinancialInstrumentIdentification <FinInstrmId>
Presence: [1..1]
Definition: Identification of the financial instrument.
Impacted by: C1 "DescriptionPresenceRule", C2 "DescriptionUsageRule", C3 "ISINGuideline", C4
"ISINPresenceRule", C5 "OtherIdentificationPresenceRule"
FinancialInstrumentIdentification <FinInstrmId> contains the following elements (see
"SecurityIdentification39" on page 2945 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ISIN <ISIN> [0..1] IdentifierSet 2946
   OtherIdentification <OthrId> [0..*]  2947
     Identification <Id> [1..1] Text 2947
     Suffix <Sfx> [0..1] Text 2947
     Type <Tp> [1..1] ± 2947
   Description <Desc> [0..1] Text 2947
Constraints
• DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification must be
present.
On Condition
    /Description is absent
Following Must be True
    /ISIN Must be present
 Or    /OtherIdentification[*] Must be present
• DescriptionUsageRule
Description must be used alone as the last resort.
• ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
• ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification must be
present.
On Condition
    /ISIN is absent
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.013.001.01 SecurityDeletionRequestV01
Target2-Securities 2041 August 2026
```

