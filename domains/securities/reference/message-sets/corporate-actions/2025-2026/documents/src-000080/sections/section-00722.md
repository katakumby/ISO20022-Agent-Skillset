---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.15 Miscellaneous", "16.1.15.15 CorporateActionOption41Choice", "16.1.15.15.2 Proprietary <Prtry>"]
file_pages: [915]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.15.15.2 Proprietary <Prtry>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 915 to 915.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 915

```text
CodeName Name Definition
International Central Securities
Depositories (ICSDs) to common
depositories who are holding the global
certificate on behalf of the International
Central Securities Depositories (ICSDs)).
MPUT Retain Option that allows a holder to elect to
retain their holding, for example, a
putable bond.
NOAC NoAction Option for the account owner not to take
part in the event. This would include opt-
out for class actions and lodging of
dissenters' rights.
NOQU NonQualifiedInvestor Account owner is a non-qualified
investor.
OFFR ProposedRate In a remarketing of variable notes, the
margin that shareholders can propose in
respect of the next interest period.
OTHR Other Generic corporate action option to be
used in case that no other specific code
is appropriate.
OVER Oversubscribe Subscribe to more equities than
underlying securities position allows.
QINV QualifiedInvestor Account owner is a qualified investor.
SECU Security Distribution of securities to holders.
SLLE SellEntitlement Sell the intermediate securities.
TAXI TaxInstruction Tax instruction.
PRUN UnknownProceeds Proceeds not known during election
period. The option can result in cash
and/or securities.
BOBD BeneficialOwnerBreakdownRequest Breakdown of beneficial ownership
required for withholding tax reclaim
event.
16.1.15.15.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Proprietary identification of the type of corporate action option.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 879 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 879
   Issuer <Issr> [1..1] Text 879
   SchemeName <SchmeNm> [0..1] Text 880
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 915 February 2026
```

