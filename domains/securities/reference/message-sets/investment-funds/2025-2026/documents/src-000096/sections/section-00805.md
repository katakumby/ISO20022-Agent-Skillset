---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["35 sese.012.001.12 PortfolioTransferInstructionV12", "35.4 Message Building Blocks", "35.4.12 NomineeAccount <NmneeAcct>", "35.4.14.10 FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf>", "35.4.14.10.25 SettlementPartiesDetails <SttlmPtiesDtls>", "35.4.14.10.25.1 SafekeepingPlace <SfkpgPlc>"]
file_pages: [1093]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.012.001.12"]
---

# 35.4.14.10.25.1 SafekeepingPlace <SfkpgPlc>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1093 to 1093.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1093

```text
SettlementPartiesDetails <SttlmPtiesDtls> contains the following FundSettlementParameters24
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SafekeepingPlace <SfkpgPlc> [0..1] ± 1093
   TradeTransactionCondition <TradTxCond> [0..*] ± 1094
   SettlementTransactionCondition <SttlmTxCond> [0..*] ± 1094
   SecuritiesSettlementSystemIdentification
<SctiesSttlmSysId>
[0..1] Text 1094
   ReceivingSideDetails <RcvgSdDtls> [0..1]  C11,
C19,
C37,
C38,
C39,
C40,
C42
1095
     Depository <Dpstry> [0..1] ± 1096
     Party1 <Pty1> [0..1] ± 1097
     Party2 <Pty2> [0..1] ± 1097
     Party3 <Pty3> [0..1] ± 1098
     Party4 <Pty4> [0..1] ± 1098
     Party5 <Pty5> [0..1] ± 1099
   DeliveringSideDetails <DlvrgSdDtls> [0..1]  C11,
C19,
C37,
C38,
C39,
C40,
C42
1099
     Depository <Dpstry> [0..1] ± 1101
     Party1 <Pty1> [0..1] ± 1102
     Party2 <Pty2> [0..1] ± 1102
     Party3 <Pty3> [0..1] ± 1102
     Party4 <Pty4> [0..1] ± 1103
     Party5 <Pty5> [0..1] ± 1103
35.4.14.10.25.1  SafekeepingPlace <SfkpgPlc>
Presence: [0..1]
Definition: Place where the securities are safe-kept, physically or notionally. This place can be, for
example, a local custodian, a Central Securities Depository or an International Central Securities
Depository.
Approved by the Securities SEG on 27 January 2026 sese.012.001.12 PortfolioTransferInstructionV12
Investment Funds - Maintenance 2025 - 2026 1093 May 2026
```

