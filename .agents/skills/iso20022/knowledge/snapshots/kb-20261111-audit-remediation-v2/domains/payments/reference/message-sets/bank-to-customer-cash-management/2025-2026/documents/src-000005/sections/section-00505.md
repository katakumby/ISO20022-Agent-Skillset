---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.2.14 Entry <Ntry>", "4.4.2.14.18 EntryDetails <NtryDtls>", "4.4.2.14.18.2 TransactionDetails <TxDtls>", "4.4.2.14.18.2.20 Tax <Tax>", "4.4.2.14.18.2.20.4 AdministrationZone <AdmstnZone>"]
file_pages: [734]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.054.001.14"]
---

# 4.4.2.14.18.2.20.4 AdministrationZone <AdmstnZone>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 734 to 734.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 734

```text
UltimateDebtor <UltmtDbtr> contains the following elements (see "TaxParty2" on page 883 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TaxIdentification <TaxId> [0..1] Text 883
   RegistrationIdentification <RegnId> [0..1] Text 883
   TaxType <TaxTp> [0..1] Text 883
   Authorisation <Authstn> [0..1]  884
     Title <Titl> [0..1] Text 884
     Name <Nm> [0..1] Text 884
4.4.2.14.18.2.20.4  AdministrationZone <AdmstnZone>
Presence: [0..1]
Definition: Territorial part of a country to which the tax payment is related.
Datatype: "Max35Text" on page 916
4.4.2.14.18.2.20.5  ReferenceNumber <RefNb>
Presence: [0..1]
Definition: Tax reference information that is specific to a taxing agency.
Datatype: "Max140Text" on page 914
4.4.2.14.18.2.20.6  Method <Mtd>
Presence: [0..1]
Definition: Method used to indicate the underlying business or how the tax is paid.
Datatype: "Max35Text" on page 916
4.4.2.14.18.2.20.7  TotalTaxableBaseAmount <TtlTaxblBaseAmt>
Presence: [0..1]
Definition: Total amount of money on which the tax is based.
Impacted by: C2 "ActiveOrHistoricCurrency", C6 "CurrencyAmount"
Datatype: "ActiveOrHistoricCurrencyAndAmount" on page 886
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
734 March 2026
```

