---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["6 auth.033.001.03 FinancialInstrumentReportingNonEquityTransparencyDataReportV03", "6.4 Message Building Blocks", "6.4.2 NonEquityTransparencyData <NonEqtyTrnsprncyData>", "6.4.2.9 DerivativeContractType <DerivCtrctTp>"]
file_pages: [64]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.033.001.03"]
---

# 6.4.2.9 DerivativeContractType <DerivCtrctTp>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 64 to 64.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 64

```text
Definition: Details on the type of asset class a non-equity financial instrument can be classified as.
Datatype: "ExternalProductType1Code" on page 437
6.4.2.9  DerivativeContractType <DerivCtrctTp>
Presence: [0..1]
Definition: Details on the contract type a derivative non-equity financial instrument can be classified as.
Datatype: "FinancialInstrumentContractType1Code" on page 437
CodeName Name Definition
CFDS ContractForDifference Contract of type contracts for difference.
FORW Forward Contract of type forward.
FRAS ForwardRateAgreement Contract of type forward rate agreement.
FUTR Futures Contract of type future.
OPTN Option Contract of type option.
OTHR Other Contract of other financial instrument
contract type.
SPDB SpreadBetting Contract of type spread betting.
SWAP Swap Contract of type swap.
SWPT Swaption Contract of type swaption.
FONS FuturesOnSwap Contract of type future on a swap.
PSWP PortfolioSwap Contract of type portfolio swap.
FFAS ForwardFreightAgreement Contract of type forward freight
agreement.
FWOS ForwardsOnASwap Contract of type forwards on a swap.
6.4.2.10  Bond <Bd>
Presence: [0..1]
Definition: Details specific to a bond / debt instrument.
Bond <Bd> contains the following elements (see "DebtInstrument5" on page 414 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] CodeSet 414
   IssuanceDate <IssncDt> [1..1] Date 414
6.4.2.11  EmissionAllowanceType <EmssnAllwncTp>
Presence: [0..1]
Definition: Details the reporting of the emission allowance sub type.
Datatype: "ExternalEmissionAllowanceSubProductType1Code" on page 436
Approved by the Securities SEG on 17 July 2025 auth.033.001.03
FinancialInstrumentReportingNonEquityTransparen
cyDataReportV03
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
64 July 2025
```

