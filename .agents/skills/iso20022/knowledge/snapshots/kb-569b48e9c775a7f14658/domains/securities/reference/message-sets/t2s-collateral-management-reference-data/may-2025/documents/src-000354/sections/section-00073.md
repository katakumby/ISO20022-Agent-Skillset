---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CollateralManagementReferenceData"
source_ids: ["src-000354"]
source_editions: ["may-2025"]
message_ids: []
heading_path: ["10 Message Items Types", "10.2 Message Datatypes", "10.2.2 CodeSet", "10.2.2.2 ActiveOrHistoricCurrencyCode"]
file_pages: [78]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 10.2.2.2 ActiveOrHistoricCurrencyCode

Source: [src-000354](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralManagementReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_CollateralManagementReferenceData_v1.pdf`. Locator: one-based file pages 78 to 78.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 78

```text
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
10.2.2.2  ActiveOrHistoricCurrencyCode
Definition: A code allocated to a currency by a Maintenance Agency under an international identification
scheme, as described in the latest edition of the international standard ISO 4217 "Codes for the
representation of currencies and funds".
Type: CodeSet
Format
pattern [A-Z]{3,3}
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
10.2.2.3  AddressType2Code
Definition: Specifies the type of address.
Type: CodeSet
CodeName Name Definition
ADDR Postal Address is the complete postal address.
PBOX POBox Address is a postal office (PO) box.
HOME Residential Address is the home address.
BIZZ Business Address is the business address.
MLTO MailTo Address is the address to which mail is
sent.
DLVY DeliveryTo Address is the address to which delivery
is to take place.
10.2.2.4  CountryCode
Definition: Code to identify a country, a dependency, or another area of particular geopolitical interest,
on the basis of country names obtained from the United Nations (ISO 3166, Alpha-2 code).
Type: CodeSet
Format
pattern [A-Z]{2,2}
Approved by the Securities SEG on 17 April 2025. Message Items Types
Target2-Securities - Collateral Management Reference Data 78 May 2025
```

