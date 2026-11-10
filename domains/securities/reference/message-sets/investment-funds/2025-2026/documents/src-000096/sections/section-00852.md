---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["35 sese.012.001.12 PortfolioTransferInstructionV12", "36.4 Message Building Blocks", "36.4.12 TransferorAccount <TrfrAcct>", "36.4.15.5 Portfolio <Prtfl>", "36.4.15.5.3 Pension <Pnsn>", "36.4.15.5.3.26 BenefitCrystallisationEventOccurred <BnftCrstllstnEvtOcrd>"]
file_pages: [1179]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.013.001.12"]
---

# 36.4.15.5.3.26 BenefitCrystallisationEventOccurred <BnftCrstllstnEvtOcrd>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1179 to 1179.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1179

```text
• Meaning When True: Yes
• Meaning When False: No
36.4.15.5.3.26  BenefitCrystallisationEventOccurred <BnftCrstllstnEvtOcrd>
Presence: [0..1]
Definition: Indicates whether a benefit crystallisation event (BCE) has occurred. This includes 'age 75
checks'.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
36.4.15.5.3.27  NonWrapperTransfer <NonWrpprTrf>
Presence: [0..1]
Definition: Indicates that the transfer is only in relation to underlying assets, and that the wrapper
transfer will occur separately.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
36.4.15.5.3.28  AdditionalInformation <AddtlInf>
Presence: [0..*]
Definition: Additional information about the pension policy, plan or scheme.
AdditionalInformation <AddtlInf> contains the following elements (see "AdditionalInformation15" on
page 4508 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InformationType <InfTp> [1..1] ± 4508
   InformationValue <InfVal> [1..1] Text 4508
36.4.15.6  AllOtherCash <AllOthrCsh>
Presence: [0..*]
Definition: Specifies whether all remaining assets in the portfolio not listed for transfer should be
liquidated and transferred as cash.
AllOtherCash <AllOthrCsh> contains the following elements (see "AllOtherCash1" on page 4866 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Indicator <Ind> [1..1] Indicator 4866
   Currency <Ccy> [0..1] CodeSet C1 4867
Approved by the Securities SEG on 27 January 2026 sese.013.001.12 PortfolioTransferConfirmationV12
Investment Funds - Maintenance 2025 - 2026 1179 May 2026
```

