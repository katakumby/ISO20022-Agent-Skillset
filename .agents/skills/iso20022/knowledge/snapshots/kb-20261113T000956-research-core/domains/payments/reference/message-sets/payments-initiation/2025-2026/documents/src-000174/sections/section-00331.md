---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pain.007.001.13 CustomerPaymentReversalV13", "5.4 Message Building Blocks", "5.4.2.18 DirectDebitTransactionInformation <DrctDbtTxInf>", "5.4.2.18.15 Tax <Tax>", "5.4.2.18.15.4 AdministrationZone <AdmstnZone>"]
file_pages: [473]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.008.001.12"]
---

# 5.4.2.18.15.4 AdministrationZone <AdmstnZone>

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 473 to 473.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 473

```text
UltimateDebtor <UltmtDbtr> contains the following elements (see "TaxParty2" on page 583 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TaxIdentification <TaxId> [0..1] Text 583
   RegistrationIdentification <RegnId> [0..1] Text 583
   TaxType <TaxTp> [0..1] Text 583
   Authorisation <Authstn> [0..1]  584
     Title <Titl> [0..1] Text 584
     Name <Nm> [0..1] Text 584
5.4.2.18.15.4  AdministrationZone <AdmstnZone>
Presence: [0..1]
Definition: Territorial part of a country to which the tax payment is related.
Datatype: "Max35Text" on page 609
5.4.2.18.15.5  ReferenceNumber <RefNb>
Presence: [0..1]
Definition: Tax reference information that is specific to a taxing agency.
Datatype: "Max140Text" on page 608
5.4.2.18.15.6  Method <Mtd>
Presence: [0..1]
Definition: Method used to indicate the underlying business or how the tax is paid.
Datatype: "Max35Text" on page 609
5.4.2.18.15.7  TotalTaxableBaseAmount <TtlTaxblBaseAmt>
Presence: [0..1]
Definition: Total amount of money on which the tax is based.
Impacted by: C2 "ActiveOrHistoricCurrency", C12 "CurrencyAmount"
Datatype: "ActiveOrHistoricCurrencyAndAmount" on page 585
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Approved by the Payments SEG on 12 January 2026 pain.008.001.12 CustomerDirectDebitInitiationV12
Payments Initiation - Maintenance 2025 - 2026 473 March 2026
```

