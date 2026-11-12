---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.13 Regulatory Reporting", "22.1.13.2 SecuritiesTransactionReport7", "22.1.13.2.9 FinancialInstrument <FinInstrm>", "22.1.13.2.9.3 Other <Othr>", "22.1.13.2.9.3.3 DerivativeInstrumentAttributes <DerivInstrmAttrbts>", "22.1.13.2.9.3.3.5 StrikePrice <StrkPric>"]
file_pages: [386]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.13.2.9.3.3.5 StrikePrice <StrkPric>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 386 to 386.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 386

```text
CodeName Name Definition
CALL Call Right to buy a quantity of an asset for an
agreed price at exercise date.
PUTO Put Right to sell a quantity of an asset for an
agreed price at exercise date.
OTHR Other Right where the holder of the option
decides whether the option is put or call.
22.1.13.2.9.3.3.5  StrikePrice <StrkPric>
Presence: [0..1]
Definition: Predetermined price at which the holder will have to buy or sell the underlying instrument.
StrikePrice <StrkPric> contains one of the following elements (see
"SecuritiesTransactionPrice4Choice" on page 350 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Price <Pric> [1..1] ± 351
Or}   NoPrice <NoPric> [1..1] ± 351
22.1.13.2.9.3.3.6  OptionExerciseStyle <OptnExrcStyle>
Presence: [0..1]
Definition: Indication as to whether the option may be exercised only at a fixed date (European, and
Asian style), a series of pre-specified dates (Bermudan) or at any time during the life of the contract
(American style). This field does not have to be populated for ISIN instruments.
Datatype: "OptionStyle7Code" on page 442
CodeName Name Definition
AMER American Option can be exercised before or on
expiry date.
ASIA Asian Option where the payoff is not
determined by the underlying price at
maturity but by the average underlying
price over some pre-set period of time.
BERM Bermudan Option that can be exercised on multiple
discrete dates prior to, or on expiry date.
EURO European Option that can be exercised on expiry
date only.
OTHR Other Other type of option style.
22.1.13.2.9.3.3.7  DeliveryType <DlvryTp>
Presence: [1..1]
Definition: Indicates whether the transaction is settled physically or in cash.
Datatype: "PhysicalTransferType4Code" on page 443
CodeName Name Definition
PHYS Physical Physical transfer.
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
386 July 2025
```

