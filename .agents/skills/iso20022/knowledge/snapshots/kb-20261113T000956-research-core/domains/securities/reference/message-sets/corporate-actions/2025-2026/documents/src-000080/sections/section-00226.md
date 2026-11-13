---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["5 seev.033.001.14 CorporateActionInstructionV14", "5.4 Message Building Blocks", "5.4.8 BeneficialOwnerDetails <BnfclOwnrDtls>", "5.4.8.3 DomicileCountry <DmclCtry>"]
file_pages: [302]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.033.001.14"]
---

# 5.4.8.3 DomicileCountry <DmclCtry>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 302 to 302.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 302

```text
5.4.8.3  DomicileCountry <DmclCtry>
Presence: [0..1]
Definition: Country in which a person is permanently domiciled (the place of a person's permanent
home).
Impacted by: C8 "Country"
Datatype: "CountryCode" on page 1205
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
5.4.8.4  NonDomicileCountry <NonDmclCtry>
Presence: [0..*]
Definition: Holder of the security certifies, in line with the terms of the corporate action, that it is not
domiciled in the country indicated.
Impacted by: C8 "Country"
Datatype: "CountryCode" on page 1205
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
5.4.8.5  OwnedSecuritiesQuantity <OwndSctiesQty>
Presence: [1..1]
Definition: Quantity of securities belonging to the beneficial owner specified.
Impacted by: C12 "DigitalTokenUnitUsageRule"
OwnedSecuritiesQuantity <OwndSctiesQty> contains one of the following elements (see
"FinancialInstrumentQuantity33Choice" on page 1091 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 1092
Or   FaceAmount <FaceAmt> [1..1] Amount 1092
Or   AmortisedValue <AmtsdVal> [1..1] Amount 1092
Or}   DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 1092
Approved by the Securities SEG on 27 January 2026 seev.033.001.14 CorporateActionInstructionV14
Corporate Actions - Maintenance 2025 - 2026 302 February 2026
```

