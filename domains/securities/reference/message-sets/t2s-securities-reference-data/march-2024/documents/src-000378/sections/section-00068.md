---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["8 reda.013.001.01 SecurityDeletionRequestV01", "8.4 Message Building Blocks", "8.4.2 FinancialInstrumentIdentification <FinInstrmId>"]
file_pages: [117]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.013.001.01"]
---

# 8.4.2 FinancialInstrumentIdentification <FinInstrmId>

Source: [src-000378](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 117 to 117.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 117

```text
MessageHeader <MsgHdr> contains the following elements (see "MessageHeader1" on page 481 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 481
   CreationDateTime <CreDtTm> [0..1] DateTime 481
8.4.2 FinancialInstrumentIdentification <FinInstrmId>
Presence: [1..1]
Definition: Identification of the financial instrument.
Impacted by: C1 "DescriptionPresenceRule", C2 "DescriptionUsageRule", C3 "ISINGuideline", C4
"ISINPresenceRule", C5 "OtherIdentificationPresenceRule"
FinancialInstrumentIdentification <FinInstrmId> contains the following elements (see
"SecurityIdentification39" on page 474 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ISIN <ISIN> [0..1] IdentifierSet 475
   OtherIdentification <OthrId> [0..*]  475
     Identification <Id> [1..1] Text 475
     Suffix <Sfx> [0..1] Text 475
     Type <Tp> [1..1] ± 475
   Description <Desc> [0..1] Text 476
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
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
reda.013.001.01 SecurityDeletionRequestV01
Target2-Securities - Securities Reference Data 117 March 2024
```

