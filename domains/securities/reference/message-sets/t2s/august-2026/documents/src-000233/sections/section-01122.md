---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["28 reda.007.001.01 SecurityMaintenanceRequestV01", "28.4 Message Building Blocks", "28.4.2 UpdateType <UpdTp>", "28.4.2.2 Replace <Rplc>", "28.4.2.2.1 FinancialInstrumentType <FinInstrmTp>", "28.4.2.2.1.3 Debt <Debt>", "28.4.2.2.1.3.54 InstrumentStructureType <InstrmStrTp>", "28.4.2.2.1.3.54.1 Code <Cd>"]
file_pages: [1619]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# 28.4.2.2.1.3.54.1 Code <Cd>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 1619 to 1619.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1619

```text
InstrumentStructureType <InstrmStrTp> contains one of the following
InstrumentSubStructureType2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1619
Or}   Proprietary <Prtry> [1..1] ± 1620
28.4.2.2.1.3.54.1  Code <Cd>
Presence: [1..1]
Definition: Instrument sub-structure type expressed as an ISO 20022 code.
Datatype: "InstrumentSubStructureType1Code" on page 3256
CodeName Name Definition
ABSE AssetBackedSecurity Sub structured type of the financial
instrument is an asset backed security.
AIRT AirlineTrust Sub structured type of the financial
instrument is an airline trust.
AUTT AutoTrust Sub structured type of the financial
instrument is an auto trust.
CBOB CollateralBondObligation Sub structured type of the financial
instrument is a collateral bond obligation.
CDOB CollateralDebtObligation Sub structured type of the financial
instrument is a collateral debt obligation.
CLNO CreditLinkedNotes Sub-structured type of the financial
instrument is a credit linked note.
CLOB CollateralLoanObligation Sub structured type of the financial
instrument is a collateral loan obligation.
CMBS CommercialMortgage Sub structured type of the financial
instrument is a commercial mortgage.
CSMR Consumer Sub structured type of the financial
instrument is a consumer.
CRCT CreditCardTrust Sub structured type of the financial
instrument is a credit card trust.
HELO HomeEquityLoans Sub structured type of the financial
instrument is a home equity loan.
LPNO LoanParticipationNote Sub structured type of the financial
instrument is a loan participation notes.
PFAB CoveredBond Sub structured type of the financial
instrument is a covered bond.
PYRT PaymentRight Sub structured type of the financial
instrument is a payment right.
REPK Repackagings Sub structured type of the financial
instrument is a repackaging.
RMBS ResidentialMortgage Sub structured type of the financial
instrument is a residential mortgage.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1619 August 2026
```

