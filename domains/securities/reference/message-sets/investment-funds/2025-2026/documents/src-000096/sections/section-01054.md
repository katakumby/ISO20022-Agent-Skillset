---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "39.4 Message Building Blocks", "39.4.7 SecondaryIndividualInvestor <ScndryIndvInvstr>", "39.4.15.1 MasterReference <MstrRef>"]
file_pages: [1459]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.019.001.09"]
---

# 39.4.15.1 MasterReference <MstrRef>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1459 to 1459.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1459

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       Servicer <Svcr> [0..1] ± 1479
       SubAccountDetails <SubAcctDtls> [0..1] ± 1480
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 1480
     SettlementPartiesDetails <SttlmPtiesDtls> [0..1]  1480
       SafekeepingPlace <SfkpgPlc> [0..1] ± 1481
       TradeTransactionCondition <TradTxCond> [0..*] ± 1482
       SettlementTransactionCondition <SttlmTxCond> [0..*] ± 1482
       SecuritiesSettlementSystemIdentification
<SctiesSttlmSysId>
[0..1] Text 1482
       ReceivingSideDetails <RcvgSdDtls> [0..1]  C6, C11,
C17,
C18,
C19,
C20,
C21
1482
         Depository <Dpstry> [0..1] ± 1484
         Party1 <Pty1> [0..1] ± 1485
         Party2 <Pty2> [0..1] ± 1485
         Party3 <Pty3> [0..1] ± 1485
         Party4 <Pty4> [0..1] ± 1486
         Party5 <Pty5> [0..1] ± 1486
     AssetsHeldInOwnName <AsstsHeldInOwnNm> [0..1] Indicator 1487
     TransferResultsInChangeOfBeneficialOwner
<TrfRsltsInChngOfBnfclOwnr>
[0..1] Indicator 1487
     AdditionalInformation <AddtlInf> [0..*] ± 1487
   AdditionalInformation <AddtlInf> [0..*] ± 1487
39.4.15.1  MasterReference <MstrRef>
Presence: [0..1]
Definition: Unique and unambiguous identifier for a group of individual transfers as assigned by the
instructing party. This identifier links the individual transfers together.
Datatype: "Max35Text" on page 5403
39.4.15.2  TransferIdentification <TrfId>
Presence: [1..1]
Definition: Identification assigned to the transfer of assets.
Datatype: "Max35Text" on page 5403
Approved by the Securities SEG on 27 January 2026 sese.019.001.09
AccountHoldingInformationRequestV09
Investment Funds - Maintenance 2025 - 2026 1459 May 2026
```

