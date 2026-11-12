---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["55 setr.015.001.05 SwitchOrderConfirmationV05", "55.4 Message Building Blocks", "55.4.4 RelatedReference <RltdRef>", "55.4.5.1 AmendmentIndicator <AmdmntInd>"]
file_pages: [3850]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.015.001.05"]
---

# 55.4.5.1 AmendmentIndicator <AmdmntInd>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3850 to 3850.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3850

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CustomerConductClassification <CstmrCndctClssfctn> [0..1] ± 4106
   TransactionChannelType <TxChanlTp> [0..1] ± 4107
   SignatureType <SgntrTp> [0..1] ± 4107
   OrderWaiverDetails <OrdrWvrDtls> [0..1] ± C37 4107
Constraints
• InvestmentAccountDetailsRule
Either InvestmentAccountDetails or all occurrences of SubscriptionLegDetails/
InvestmentAccountDetails and RedemptionLegDetails/InvestmentAccountDetails must be present,
but not both.
• OrderOriginatorEligibility3Rule
Either InvestmentAccountDetails/OrderOriginatorEligibility or a single occurrence of
RedemptionLegDetails/InvestmentAccountDetails/OrderOriginatorEligibility or a single occurrence of
SubscriptionLegDetails/InvestmentAccountDetails/OrderOriginatorEligibility should be only present.
55.4.5.1  AmendmentIndicator <AmdmntInd>
Presence: [0..1]
Definition: Indicates whether the confirmation is an amendment of a previous confirmation.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
55.4.5.2  MasterReference <MstrRef>
Presence: [0..1]
Definition: Unique and unambiguous identifier for a group of individual orders, as assigned by the
instructing party. This identifier links the individual orders together.
Datatype: "Max35Text" on page 5403
55.4.5.3  PlaceOfTrade <PlcOfTrad>
Presence: [0..1]
Definition: Market in which the advised trade transaction was executed.
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 3850 May 2026
```

