---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["44 reda.024.001.01 CollateralValueCreationRequestV01", "44.4 Message Building Blocks", "44.4.2 CollateralValue <CollVal>", "44.4.2.9 CloseLinkHaircut <ClsLkHrcut>"]
file_pages: [2171]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.024.001.01"]
---

# 44.4.2.9 CloseLinkHaircut <ClsLkHrcut>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2171 to 2171.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2171

```text
Definition: Haircut or valuation factor on the security expressed as a percentage.
Datatype: "PercentageRate" on page 3325
44.4.2.9  CloseLinkHaircut <ClsLkHrcut>
Presence: [0..1]
Definition: Haircut or valuation factor on the security expressed as a percentage in case of close links.
Datatype: "PercentageRate" on page 3325
44.4.2.10  PoolFactor <PoolFctr>
Presence: [0..1]
Definition: Percentage that applies to price of the securities following a redemption.
Datatype: "PercentageRate" on page 3325
44.4.2.11  ForeignExchange <FX>
Presence: [0..1]
Definition: Information needed to process a currency exchange or conversion.
ForeignExchange <FX> contains the following elements (see "ForeignExchangeTerms23" on
page 3021 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   UnitCurrency <UnitCcy> [1..1] CodeSet C1 3022
   QuotedCurrency <QtdCcy> [1..1] CodeSet C1 3022
   ExchangeRate <XchgRate> [1..1] Rate 3022
   ResultingAmount <RsltgAmt> [1..1] Amount C1, C4 3023
44.4.3 PartyIdentification <PtyId>
Presence: [1..1]
Definition: Identifies the party for which the eligible security is defined.
PartyIdentification <PtyId> contains one of the following SystemPartyIdentification2Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   OrganisationIdentification <OrgId> [1..1] ± 2171
Or}   CombinedIdentification <CmbndId> [1..1] ± 2172
44.4.3.1  OrganisationIdentification <OrgId>
Presence: [1..1]
Definition: Provides the identification of a party.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.024.001.01
CollateralValueCreationRequestV01
Target2-Securities 2171 August 2026
```

