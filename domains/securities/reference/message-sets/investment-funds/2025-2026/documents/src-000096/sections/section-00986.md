---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "38.4 Message Building Blocks", "38.4.10 SecondaryCorporateInvestor <ScndryCorpInvstr>", "38.4.15.4 Portfolio <Prtfl>", "38.4.15.4.3 Pension <Pnsn>", "38.4.15.4.3.11 BlockTransferReference <BlckTrfRef>"]
file_pages: [1368]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.018.001.10"]
---

# 38.4.15.4.3.11 BlockTransferReference <BlckTrfRef>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1368 to 1368.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1368

```text
38.4.15.4.3.11  BlockTransferReference <BlckTrfRef>
Presence: [0..1]
Definition: When the transfer is part of a block transfer, reference to link several items.
Datatype: "Max35Text" on page 5403
38.4.15.4.3.12  TaxFreeCashProtection <TaxFreeCshPrtcn>
Presence: [0..1]
Definition: Indicates whether the tax-free cash is protected when the pension policy, plan or scheme is
transferred.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
38.4.15.4.3.13  TaxFreeCashAmount <TaxFreeCshAmt>
Presence: [0..1]
Definition: Amount of cash that is tax free.
TaxFreeCashAmount <TaxFreeCshAmt> contains the following elements (see "DateAndAmount2" on
page 4343 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Date <Dt> [0..1] Date 4343
   Amount <Amt> [1..1] Amount C2, C10 4343
38.4.15.4.3.14  ValueOfPensionPolicyOrPlanOrScheme <ValOfPnsnPlcyOrPlanOrSchme>
Presence: [0..1]
Definition: Value of the pension policy, plan or scheme.
ValueOfPensionPolicyOrPlanOrScheme <ValOfPnsnPlcyOrPlanOrSchme> contains the following
elements (see "DateAndAmount2" on page 4343 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Date <Dt> [0..1] Date 4343
   Amount <Amt> [1..1] Amount C2, C10 4343
38.4.15.4.3.15  RetirementAgeProtection <RtrmntAgePrtcn>
Presence: [0..1]
Definition: Indicates whether the pension policy, plan or scheme has retirement age protection.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
Approved by the Securities SEG on 27 January 2026 sese.018.001.10 AccountHoldingInformationV10
Investment Funds - Maintenance 2025 - 2026 1368 May 2026
```

