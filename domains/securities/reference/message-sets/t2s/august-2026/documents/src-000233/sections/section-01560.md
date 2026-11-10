---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["46 reda.026.001.01 EligibleCounterpartCSDCreationRequestV01", "46.4 Message Building Blocks", "46.4.2 EligibleCounterpartCSD <ElgblCntrptCSD>", "46.4.2.6 EligibilityIdentification <ElgbltyId>"]
file_pages: [2184]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.026.001.01"]
---

# 46.4.2.6 EligibilityIdentification <ElgbltyId>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2184 to 2184.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2184

```text
Definition: Defines the type of eligibility.
Datatype: "EligibilityType1Code" on page 3237
CodeName Name Definition
SECU Securities Eligibility applies at securities level.
ISCS IssuerCSD Eligibility applies at the level of issuer
CSD.
All of the securities issued by the issuer
CSD are eligible.
CTRY Country Eligibility applies at country level.
All of the securities issued in that country
are eligible.
46.4.2.6  EligibilityIdentification <ElgbltyId>
Presence: [1..1]
Definition: Unique identification of the eligible counterpart party.
EligibilityIdentification <ElgbltyId> contains one of the following EligibilityIdentification3Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Country <Ctry> [1..1] CodeSet C2 2184
Or   FinancialInstrumentIdentification <FinInstrmId> [1..1] IdentifierSet 2184
Or}   IssuerCSDIdentification <IssrCSDId> [1..1]  2185
{Or     OrganisationIdentification <OrgId> [1..1] ± 2185
Or}     CombinedIdentification <CmbndId> [1..1] ± 2185
46.4.2.6.1  Country <Ctry>
Presence: [1..1]
Definition: Country code used to identify the issuance country to be defined as eligible.
Impacted by: C2 "Country"
Datatype: "CountryCode" on page 3234
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
46.4.2.6.2  FinancialInstrumentIdentification <FinInstrmId>
Presence: [1..1]
Definition: ISIN used to identify the security to be defined as eligible.
Datatype: "ISINOct2015Identifier" on page 3322
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.026.001.01
EligibleCounterpartCSDCreationRequestV01
Target2-Securities 2184 August 2026
```

