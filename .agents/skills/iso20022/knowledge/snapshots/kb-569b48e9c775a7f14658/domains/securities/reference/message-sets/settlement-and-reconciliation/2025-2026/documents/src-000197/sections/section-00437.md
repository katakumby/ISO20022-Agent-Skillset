---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["20 sese.026.001.12 SecuritiesSettlementTransactionReversalAdviceV12", "20.4 Message Building Blocks", "20.4.3 AdditionalParameters <AddtlParams>", "20.4.4.17 FXAdditionalDetails <FxAddtlDtls>"]
file_pages: [673]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.026.001.12"]
---

# 20.4.4.17 FXAdditionalDetails <FxAddtlDtls>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 673 to 673.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 673

```text
20.4.4.17  FXAdditionalDetails <FxAddtlDtls>
Presence: [0..1]
Definition: Provides additional details pertaining to foreign exchange instructions.
Datatype: "Max350Text" on page 2192
20.4.4.18  SettlementInstructionProcessingAdditionalDetails
<SttlmInstrPrcgAddtlDtls>
Presence: [0..1]
Definition: Provides additional settlement processing information which cannot be included within the
structured fields of the message.
Datatype: "Max350Text" on page 2192
20.4.5 FinancialInstrumentIdentification <FinInstrmId>
Presence: [1..1]
Definition: Financial instrument representing a sum of rights of the investor vis-a-vis the issuer.
Impacted by: C18 "DescriptionPresenceRule", C19 "DescriptionUsageRule", C25 "ISINGuideline", C26
"ISINPresenceRule", C31 "OtherIdentificationPresenceRule"
FinancialInstrumentIdentification <FinInstrmId> contains the following elements (see
"SecurityIdentification19" on page 1474 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ISIN <ISIN> [0..1] IdentifierSet 1475
   OtherIdentification <OthrId> [0..*]  1475
     Identification <Id> [1..1] Text 1475
     Suffix <Sfx> [0..1] Text 1475
     Type <Tp> [1..1] ± 1476
   Description <Desc> [0..1] Text 1476
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
Approved by the Securities SEG on 27 January 2026 sese.026.001.12
SecuritiesSettlementTransactionReversalAdviceV12
Settlement And Reconciliation - Maintenance 2025 - 2026 673 March 2026
```

