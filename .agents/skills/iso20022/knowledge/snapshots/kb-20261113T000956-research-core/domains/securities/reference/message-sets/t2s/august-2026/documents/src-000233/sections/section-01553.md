---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["45 reda.025.001.01 EligibleSecuritiesCreationRequestV01", "45.4 Message Building Blocks", "45.4.2 EligibleSecurity <ElgblScty>", "45.4.2.2 CollateralisationCurrency <CollstnCcy>"]
file_pages: [2177]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.025.001.01"]
---

# 45.4.2.2 CollateralisationCurrency <CollstnCcy>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2177 to 2177.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2177

```text
45.4.2.2  CollateralisationCurrency <CollstnCcy>
Presence: [0..1]
Definition: Currency which may be processed by the system. A system may process transactions in a
single currency or in multiple currencies.
Impacted by: C1 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyCode" on page 3212
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
45.4.2.3  EligibilitySetProfile <ElgbltySetPrfl>
Presence: [0..1]
Definition: Number identifying the collateral eligibility set profile of the counterparty.
EligibilitySetProfile <ElgbltySetPrfl> contains the following elements (see "GenericIdentification1" on
page 2966 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2966
   SchemeName <SchmeNm> [0..1] Text 2966
   Issuer <Issr> [0..1] Text 2966
45.4.2.4  PartyIdentification <PtyId>
Presence: [1..1]
Definition: Identifies the party for which the eligible security is defined.
PartyIdentification <PtyId> contains one of the following SystemPartyIdentification2Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   OrganisationIdentification <OrgId> [1..1] ± 2177
Or}   CombinedIdentification <CmbndId> [1..1] ± 2178
45.4.2.4.1  OrganisationIdentification <OrgId>
Presence: [1..1]
Definition: Provides the identification of a party.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.025.001.01
EligibleSecuritiesCreationRequestV01
Target2-Securities 2177 August 2026
```

