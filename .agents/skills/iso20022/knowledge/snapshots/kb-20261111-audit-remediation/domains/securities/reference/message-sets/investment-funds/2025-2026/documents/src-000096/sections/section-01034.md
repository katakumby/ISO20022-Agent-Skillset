---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "38.4 Message Building Blocks", "38.4.10 SecondaryCorporateInvestor <ScndryCorpInvstr>", "38.4.15.8 FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf>", "38.4.15.8.15 IntermediaryInformation <IntrmyInf>"]
file_pages: [1427]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.018.001.10"]
---

# 38.4.15.8.15 IntermediaryInformation <IntrmyInf>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1427 to 1427.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1427

```text
BlockChainAddressOrWallet <BlckChainAdrOrWllt> contains the following elements (see
"BlockChainAddressWallet3" on page 4846 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4846
   Type <Tp> [0..1] ± 4846
   Name <Nm> [0..1] Text 4846
38.4.15.8.15  IntermediaryInformation <IntrmyInf>
Presence: [0..*]
Definition: Identification of a related party or intermediary.
IntermediaryInformation <IntrmyInf> contains the following elements (see "Intermediary43" on
page 5040 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 5040
   Account <Acct> [0..1]  5041
     Identification <Id> [0..1] Text 5041
     AccountServicer <AcctSvcr> [1..1] ± 5041
   Role <Role> [0..1] ± 5041
   ContactPerson <CtctPrsn> [0..1] ± 5041
38.4.15.8.16  CrystallisationDetails <CrstllstnDtls>
Presence: [0..*]
Definition: Number of units that have been received (crystallised) or not yet received (uncrystallised)
from the fund. This is typically relevant to a pension fund.
CrystallisationDetails <CrstllstnDtls> contains the following elements (see "Crystallisation2" on
page 4766 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TrancheIdentification <TrchId> [1..1] Text 4766
   CrystallisedUnitsNumber <CrstllsdUnitsNb> [0..1] Quantity 4766
   UncrystallisedUnitsNumber <UcrstllsdUnitsNb> [0..1] Quantity 4766
   CrystallisedAmount <CrstllsdAmt> [0..1] Amount C1 4766
   UncrystallisedAmount <UcrstllsdAmt> [0..1] Amount C1 4767
   AdditionalInformation <AddtlInf> [0..*] ± 4767
38.4.15.8.17  TaxValuationPoint <TaxValtnPt>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 sese.018.001.10 AccountHoldingInformationV10
Investment Funds - Maintenance 2025 - 2026 1427 May 2026
```

