---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CollateralManagementReferenceData"
source_ids: ["src-000354"]
source_editions: ["may-2025"]
message_ids: []
heading_path: ["4 reda.026.001.01 EligibleCounterpartCSDCreationRequestV01", "4.4 Message Building Blocks", "4.4.2 EligibleCounterpartCSD <ElgblCntrptCSD>", "4.4.2.6 EligibilityIdentification <ElgbltyId>"]
file_pages: [27]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.026.001.01"]
---

# 4.4.2.6 EligibilityIdentification <ElgbltyId>

Source: [src-000354](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralManagementReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_CollateralManagementReferenceData_v1.pdf`. Locator: one-based file pages 27 to 27.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 27

```text
Definition: Defines the type of eligibility.
Datatype: "EligibilityType1Code" on page 79
CodeName Name Definition
SECU Securities Eligibility applies at securities level.
ISCS IssuerCSD Eligibility applies at the level of issuer
CSD.
All of the securities issued by the issuer
CSD are eligible.
CTRY Country Eligibility applies at country level.
All of the securities issued in that country
are eligible.
4.4.2.6  EligibilityIdentification <ElgbltyId>
Presence: [1..1]
Definition: Unique identification of the eligible counterpart party.
EligibilityIdentification <ElgbltyId> contains one of the following EligibilityIdentification3Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Country <Ctry> [1..1] CodeSet C2 27
Or   FinancialInstrumentIdentification <FinInstrmId> [1..1] IdentifierSet 27
Or}   IssuerCSDIdentification <IssrCSDId> [1..1]  28
{Or     OrganisationIdentification <OrgId> [1..1] ± 28
Or}     CombinedIdentification <CmbndId> [1..1] ± 28
4.4.2.6.1  Country <Ctry>
Presence: [1..1]
Definition: Country code used to identify the issuance country to be defined as eligible.
Impacted by: C2 "Country"
Datatype: "CountryCode" on page 78
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
4.4.2.6.2  FinancialInstrumentIdentification <FinInstrmId>
Presence: [1..1]
Definition: ISIN used to identify the security to be defined as eligible.
Datatype: "ISINOct2015Identifier" on page 81
Approved by the Securities SEG on 17 April 2025. reda.026.001.01
EligibleCounterpartCSDCreationRequestV01
Target2-Securities - Collateral Management Reference Data 27 May 2025
```

