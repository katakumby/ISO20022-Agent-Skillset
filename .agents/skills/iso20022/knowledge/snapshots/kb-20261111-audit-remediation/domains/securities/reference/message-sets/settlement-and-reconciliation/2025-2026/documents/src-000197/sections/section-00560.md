---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["25 sese.031.001.11 SecuritiesSettlementConditionModificationStatusAdviceV11", "26.4 Message Building Blocks", "26.4.3 Linkages <Lnkgs>", "26.4.4.22 FXAdditionalDetails <FxAddtlDtls>"]
file_pages: [844]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.032.001.13"]
---

# 26.4.4.22 FXAdditionalDetails <FxAddtlDtls>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 844 to 844.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 844

```text
Definition: Status of affirmation of a trade.
AffirmationStatus <AffirmSts> contains one of the following elements (see
"AffirmationStatus8Choice" on page 1878 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1878
Or}   Proprietary <Prtry> [1..1] ± 1879
26.4.4.22  FXAdditionalDetails <FxAddtlDtls>
Presence: [0..1]
Definition: Provides additional details pertaining to foreign exchange instructions.
Datatype: "Max350Text" on page 2192
26.4.4.23  SettlementInstructionProcessingAdditionalDetails
<SttlmInstrPrcgAddtlDtls>
Presence: [0..1]
Definition: Provides additional settlement processing information which cannot be included within the
structured fields of the message.
Datatype: "Max350Text" on page 2192
26.4.5 FinancialInstrumentIdentification <FinInstrmId>
Presence: [1..1]
Definition: Financial instrument representing a sum of rights of the investor vis-a-vis the issuer.
Impacted by: C25 "DescriptionPresenceRule", C26 "DescriptionUsageRule", C33 "ISINGuideline", C34
"ISINPresenceRule", C41 "OtherIdentificationPresenceRule"
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
Approved by the Securities SEG on 27 January 2026 sese.032.001.13
SecuritiesSettlementTransactionGenerationNotificati
onV13
Settlement And Reconciliation - Maintenance 2025 - 2026 844 March 2026
```

