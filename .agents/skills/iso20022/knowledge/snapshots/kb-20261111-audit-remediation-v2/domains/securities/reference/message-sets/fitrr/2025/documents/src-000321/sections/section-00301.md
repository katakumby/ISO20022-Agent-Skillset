---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.11 Price", "22.1.11.2 SecuritiesTransactionPrice4Choice", "22.1.11.2.1 Price <Pric>"]
file_pages: [351]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.11.2.1 Price <Pric>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 351 to 351.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 351

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Price <Pric> [1..1] ± 351
Or}   NoPrice <NoPric> [1..1] ± 351
22.1.11.2.1  Price <Pric>
Presence: [1..1]
Definition: Predetermined price at which the holder will have to buy or sell the underlying instrument.
Price <Pric> contains one of the following elements (see "SecuritiesTransactionPrice2Choice" on
page 355 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   MonetaryValue <MntryVal> [1..1] ± 355
Or   Percentage <Pctg> [1..1] Rate 355
Or   Yield <Yld> [1..1] Rate 355
Or}   BasisPoints <BsisPts> [1..1] Quantity 356
22.1.11.2.2  NoPrice <NoPric>
Presence: [1..1]
Definition: Captures where no price is yet known.
NoPrice <NoPric> contains the following elements (see "SecuritiesTransactionPrice1" on page 354 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Pending <Pdg> [1..1] CodeSet 354
   Currency <Ccy> [0..1] CodeSet C2 354
22.1.11.3  SecuritiesTransactionPrice7
Definition: Choice to define the price of the securities transaction.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MonetaryValue <MntryVal> [1..1] ± 351
   DigitalTokenQuantity <DgtlTknQty> [1..1]  352
     Identifier <Idr> [1..1] IdentifierSet 352
     Unit <Unit> [0..1] Quantity 352
     Description <Desc> [0..1] Text 352
22.1.11.3.1  MonetaryValue <MntryVal>
Presence: [1..1]
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
351 July 2025
```

