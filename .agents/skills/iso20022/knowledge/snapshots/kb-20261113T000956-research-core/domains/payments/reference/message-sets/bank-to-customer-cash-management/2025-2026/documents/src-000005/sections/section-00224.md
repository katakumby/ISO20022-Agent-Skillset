---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "3.4 Message Building Blocks", "3.4.2 Statement <Stmt>", "3.4.2.15 Entry <Ntry>", "3.4.2.15.17 CardTransaction <CardTx>", "3.4.2.15.17.1 Card <Card>", "3.4.2.15.17.1.1 PlainCardData <PlainCardData>", "3.4.2.15.17.1.1.7 CardSecurityCode <CardSctyCd>", "3.4.2.15.17.1.1.7.2 CSCValue <CSCVal>"]
file_pages: [346]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.053.001.14"]
---

# 3.4.2.15.17.1.1.7.2 CSCValue <CSCVal>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 346 to 346.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 346

```text
3.4.2.15.17.1.1.7.2  CSCValue <CSCVal>
Presence: [0..1]
Definition: Card security code (CSC).
Datatype: "Min3Max4NumericText" on page 918
3.4.2.15.17.1.2  CardCountryCode <CardCtryCd>
Presence: [0..1]
Definition: Country code assigned to the card by the card issuer.
Datatype: "Exact3NumericText" on page 913
3.4.2.15.17.1.3  CardBrand <CardBrnd>
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
3.4.2.15.17.1.4  AdditionalCardData <AddtlCardData>
Presence: [0..1]
Definition: Additional card issuer specific data.
Datatype: "Max70Text" on page 917
3.4.2.15.17.2  POI <POI>
Presence: [0..1]
Definition: Physical or logical card payment terminal containing software and hardware components.
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
346 March 2026
```

