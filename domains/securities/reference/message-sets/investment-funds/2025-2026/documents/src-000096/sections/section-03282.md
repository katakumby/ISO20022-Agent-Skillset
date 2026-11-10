---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.18 Financial Instrument", "66.1.18.14 FinancialInstrument13", "66.1.18.14.5 SecuritiesForm <SctiesForm>"]
file_pages: [4519]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.18.14.5 SecuritiesForm <SctiesForm>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4519 to 4519.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4519

```text
66.1.18.14.5  SecuritiesForm <SctiesForm>
Presence: [0..1]
Definition: Form, ie, ownership, of the security, eg, registered or bearer.
Datatype: "FormOfSecurity1Code" on page 5304
CodeName Name Definition
BEAR Bearer The financial instrument does not specify
any registration of ownership, and is
payable to whomever possesses the
certificate.
REGD Registered Shareholder name of the financial
instrument appears in the corporation/
funds books.
66.1.18.14.6  DistributionPolicy <DstrbtnPlcy>
Presence: [0..1]
Definition: Income policy relating to a class type, ie, if income is paid out or retained in the fund.
Datatype: "DistributionPolicy1Code" on page 5294
CodeName Name Definition
DIST Distribution Income is distributed to the investors in
the fund.
ACCU Accumulation Income is added to the capital of the
fund.
66.1.19 Financial Instrument Identification
66.1.19.1  CashAsset3
Definition: Identification of a cash asset.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CashAssetType <CshAsstTp> [1..1]  4520
{Or     Code <Cd> [1..1] CodeSet 4520
Or}     Proprietary <Prtry> [1..1] ± 4520
   HoldingCurrency <HldgCcy> [1..1] CodeSet C1 4520
   TransferCurrency <TrfCcy> [0..1] CodeSet C1 4521
   AdditionalInformation <AddtlInf> [0..1] ± 4521
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4519 May 2026
```

