---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "38.4 Message Building Blocks", "38.4.10 SecondaryCorporateInvestor <ScndryCorpInvstr>", "38.4.15.4 Portfolio <Prtfl>", "38.4.15.4.3 Pension <Pnsn>", "38.4.15.4.3.26 BenefitCrystallisationEventOccurred <BnftCrstllstnEvtOcrd>"]
file_pages: [1371]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.018.001.10"]
---

# 38.4.15.4.3.26 BenefitCrystallisationEventOccurred <BnftCrstllstnEvtOcrd>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1371 to 1371.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1371

```text
• Meaning When True: Yes
• Meaning When False: No
38.4.15.4.3.26  BenefitCrystallisationEventOccurred <BnftCrstllstnEvtOcrd>
Presence: [0..1]
Definition: Indicates whether a benefit crystallisation event (BCE) has occurred. This includes 'age 75
checks'.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
38.4.15.4.3.27  NonWrapperTransfer <NonWrpprTrf>
Presence: [0..1]
Definition: Indicates that the transfer is only in relation to underlying assets, and that the wrapper
transfer will occur separately.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
38.4.15.4.3.28  AdditionalInformation <AddtlInf>
Presence: [0..*]
Definition: Additional information about the pension policy, plan or scheme.
AdditionalInformation <AddtlInf> contains the following elements (see "AdditionalInformation15" on
page 4508 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InformationType <InfTp> [1..1] ± 4508
   InformationValue <InfVal> [1..1] Text 4508
38.4.15.5  PartialDiscovery <PrtlDscvry>
Presence: [0..1]
Definition: Indicates that not all the assets in the holding/portfolio are specified and that some other kind
of other communication is required.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
38.4.15.6  ResidualCash <RsdlCsh>
Presence: [0..*]
Definition: Specifies whether there is cash in the account awaiting investment and the currency.
Approved by the Securities SEG on 27 January 2026 sese.018.001.10 AccountHoldingInformationV10
Investment Funds - Maintenance 2025 - 2026 1371 May 2026
```

