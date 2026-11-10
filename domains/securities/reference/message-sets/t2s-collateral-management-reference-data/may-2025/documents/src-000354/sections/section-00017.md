---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CollateralManagementReferenceData"
source_ids: ["src-000354"]
source_editions: ["may-2025"]
message_ids: []
heading_path: ["3 reda.025.001.01 EligibleSecuritiesCreationRequestV01", "3.4 Message Building Blocks", "3.4.2 EligibleSecurity <ElgblScty>", "3.4.2.2 CollateralisationCurrency <CollstnCcy>"]
file_pages: [20]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.025.001.01"]
---

# 3.4.2.2 CollateralisationCurrency <CollstnCcy>

Source: [src-000354](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralManagementReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_CollateralManagementReferenceData_v1.pdf`. Locator: one-based file pages 20 to 20.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 20

```text
3.4.2.2  CollateralisationCurrency <CollstnCcy>
Presence: [0..1]
Definition: Currency which may be processed by the system. A system may process transactions in a
single currency or in multiple currencies.
Impacted by: C1 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyCode" on page 78
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
3.4.2.3  EligibilitySetProfile <ElgbltySetPrfl>
Presence: [0..1]
Definition: Number identifying the collateral eligibility set profile of the counterparty.
EligibilitySetProfile <ElgbltySetPrfl> contains the following elements (see "GenericIdentification1" on
page 65 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 65
   SchemeName <SchmeNm> [0..1] Text 65
   Issuer <Issr> [0..1] Text 65
3.4.2.4  PartyIdentification <PtyId>
Presence: [1..1]
Definition: Identifies the party for which the eligible security is defined.
PartyIdentification <PtyId> contains one of the following SystemPartyIdentification2Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   OrganisationIdentification <OrgId> [1..1] ± 20
Or}   CombinedIdentification <CmbndId> [1..1] ± 21
3.4.2.4.1  OrganisationIdentification <OrgId>
Presence: [1..1]
Definition: Provides the identification of a party.
Approved by the Securities SEG on 17 April 2025. reda.025.001.01
EligibleSecuritiesCreationRequestV01
Target2-Securities - Collateral Management Reference Data 20 May 2025
```

