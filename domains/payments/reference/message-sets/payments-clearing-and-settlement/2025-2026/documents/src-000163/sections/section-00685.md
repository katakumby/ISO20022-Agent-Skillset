---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 pacs.009.001.13 FinancialInstitutionCreditTransferV13", "7.4 Message Building Blocks", "7.4.2 CreditTransferTransactionInformation <CdtTrfTxInf>", "7.4.2.40 UnderlyingCustomerCreditTransfer <UndrlygCstmrCdtTrf>", "7.4.2.40.29 Tax <Tax>", "7.4.2.40.29.4 AdministrationZone <AdmstnZone>"]
file_pages: [933]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.009.001.13"]
---

# 7.4.2.40.29.4 AdministrationZone <AdmstnZone>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 933 to 933.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 933

```text
UltimateDebtor <UltmtDbtr> contains the following elements (see "TaxParty2" on page 1221 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TaxIdentification <TaxId> [0..1] Text 1221
   RegistrationIdentification <RegnId> [0..1] Text 1221
   TaxType <TaxTp> [0..1] Text 1221
   Authorisation <Authstn> [0..1]  1221
     Title <Titl> [0..1] Text 1222
     Name <Nm> [0..1] Text 1222
7.4.2.40.29.4  AdministrationZone <AdmstnZone>
Presence: [0..1]
Definition: Territorial part of a country to which the tax payment is related.
Datatype: "Max35Text" on page 1246
7.4.2.40.29.5  ReferenceNumber <RefNb>
Presence: [0..1]
Definition: Tax reference information that is specific to a taxing agency.
Datatype: "Max140Text" on page 1244
7.4.2.40.29.6  Method <Mtd>
Presence: [0..1]
Definition: Method used to indicate the underlying business or how the tax is paid.
Datatype: "Max35Text" on page 1246
7.4.2.40.29.7  TotalTaxableBaseAmount <TtlTaxblBaseAmt>
Presence: [0..1]
Definition: Total amount of money on which the tax is based.
Impacted by: C2 "ActiveOrHistoricCurrency", C9 "CurrencyAmount"
Datatype: "ActiveOrHistoricCurrencyAndAmount" on page 1223
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Approved by the Payments SEG on 12 January 2026 pacs.009.001.13
FinancialInstitutionCreditTransferV13
Payments Clearing and Settlement - Maintenance 2025 -
2026
933 March 2026
```

