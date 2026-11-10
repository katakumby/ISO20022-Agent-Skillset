---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.4 Message Building Blocks", "2.4.2 Report <Rpt>", "2.4.2.15 Entry <Ntry>", "2.4.2.15.18 EntryDetails <NtryDtls>", "2.4.2.15.18.2 TransactionDetails <TxDtls>", "2.4.2.15.18.2.26 CardTransaction <CardTx>", "2.4.2.15.18.2.26.1 Card <Card>", "2.4.2.15.18.2.26.1.1 PlainCardData <PlainCardData>", "2.4.2.15.18.2.26.1.1.7 CardSecurityCode <CardSctyCd>", "2.4.2.15.18.2.26.1.1.7.2 CSCValue <CSCVal>"]
file_pages: [240]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.052.001.14"]
---

# 2.4.2.15.18.2.26.1.1.7.2 CSCValue <CSCVal>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 240 to 240.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 240

```text
2.4.2.15.18.2.26.1.1.7.2  CSCValue <CSCVal>
Presence: [0..1]
Definition: Card security code (CSC).
Datatype: "Min3Max4NumericText" on page 918
2.4.2.15.18.2.26.1.2  CardCountryCode <CardCtryCd>
Presence: [0..1]
Definition: Country code assigned to the card by the card issuer.
Datatype: "Exact3NumericText" on page 913
2.4.2.15.18.2.26.1.3  CardBrand <CardBrnd>
Presence: [0..1]
Definition: Brand name of the card.
CardBrand <CardBrnd> contains the following elements (see "GenericIdentification1" on page 841 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 841
   SchemeName <SchmeNm> [0..1] Text 841
   Issuer <Issr> [0..1] Text 841
2.4.2.15.18.2.26.1.4  AdditionalCardData <AddtlCardData>
Presence: [0..1]
Definition: Additional card issuer specific data.
Datatype: "Max70Text" on page 917
2.4.2.15.18.2.26.2  POI <POI>
Presence: [0..1]
Definition: Physical or logical card payment terminal containing software and hardware components.
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
240 March 2026
```

