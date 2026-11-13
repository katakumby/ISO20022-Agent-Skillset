---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CollateralManagementReferenceData"
source_ids: ["src-000354"]
source_editions: ["may-2025"]
message_ids: []
heading_path: ["2 reda.024.001.01 CollateralValueCreationRequestV01", "2.4 Message Building Blocks", "2.4.2 CollateralValue <CollVal>", "2.4.2.9 CloseLinkHaircut <ClsLkHrcut>"]
file_pages: [14]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.024.001.01"]
---

# 2.4.2.9 CloseLinkHaircut <ClsLkHrcut>

Source: [src-000354](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralManagementReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_CollateralManagementReferenceData_v1.pdf`. Locator: one-based file pages 14 to 14.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 14

```text
Definition: Haircut or valuation factor on the security expressed as a percentage.
Datatype: "PercentageRate" on page 82
2.4.2.9  CloseLinkHaircut <ClsLkHrcut>
Presence: [0..1]
Definition: Haircut or valuation factor on the security expressed as a percentage in case of close links.
Datatype: "PercentageRate" on page 82
2.4.2.10  PoolFactor <PoolFctr>
Presence: [0..1]
Definition: Percentage that applies to price of the securities following a redemption.
Datatype: "PercentageRate" on page 82
2.4.2.11  ForeignExchange <FX>
Presence: [0..1]
Definition: Information needed to process a currency exchange or conversion.
ForeignExchange <FX> contains the following elements (see "ForeignExchangeTerms23" on
page 67 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   UnitCurrency <UnitCcy> [1..1] CodeSet C1 67
   QuotedCurrency <QtdCcy> [1..1] CodeSet C1 67
   ExchangeRate <XchgRate> [1..1] Rate 67
   ResultingAmount <RsltgAmt> [1..1] Amount C1, C6 68
2.4.3 PartyIdentification <PtyId>
Presence: [1..1]
Definition: Identifies the party for which the eligible security is defined.
PartyIdentification <PtyId> contains one of the following SystemPartyIdentification2Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   OrganisationIdentification <OrgId> [1..1] ± 14
Or}   CombinedIdentification <CmbndId> [1..1] ± 15
2.4.3.1  OrganisationIdentification <OrgId>
Presence: [1..1]
Definition: Provides the identification of a party.
Approved by the Securities SEG on 17 April 2025. reda.024.001.01
CollateralValueCreationRequestV01
Target2-Securities - Collateral Management Reference Data 14 May 2025
```

