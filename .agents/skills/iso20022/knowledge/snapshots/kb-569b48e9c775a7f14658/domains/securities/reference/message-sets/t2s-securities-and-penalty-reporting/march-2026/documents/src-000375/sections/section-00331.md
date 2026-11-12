---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.19 Party Identification", "7.1.19.6 Pledgee3", "7.1.19.6.1 PledgeeTypeAndIdentification <PldgeeTpAndId>", "7.1.19.6.1.1 TypeAndIdentification <TpAndId>"]
file_pages: [418]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.19.6.1.1 TypeAndIdentification <TpAndId>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 418 to 418.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 418

```text
PledgeeTypeAndIdentification <PldgeeTpAndId> contains one of the following
PledgeeFormat5Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   TypeAndIdentification <TpAndId> [1..1]  418
     Identification <Id> [1..1] IdentifierSet C2 418
     PledgeeType <PldgeeTp> [1..1] CodeSet 418
Or   Identification <Id> [1..1]  419
     Identification <Id> [0..1] Text 419
     PledgeeType <PldgeeTp> [1..1] CodeSet 419
Or}   Proprietary <Prtry> [1..1] ± 419
7.1.19.6.1.1  TypeAndIdentification <TpAndId>
Presence: [1..1]
Definition: Identification of the entity to which the financial instruments are pledged expressed as a code
and a BIC.
TypeAndIdentification <TpAndId> contains the following PledgeeTypeAndAnyBICIdentifier2
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] IdentifierSet C2 418
   PledgeeType <PldgeeTp> [1..1] CodeSet 418
7.1.19.6.1.1.1  Identification <Id>
Presence: [1..1]
Definition: Identification of the entity to which the financial instruments are pledged, expressed as a BIC.
Impacted by: C2 "AnyBIC"
Datatype: "AnyBICDec2014Identifier" on page 551
Constraints
• AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the ISO
directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
7.1.19.6.1.1.2  PledgeeType <PldgeeTp>
Presence: [1..1]
Definition: Entity to which the financial instruments are pledged expressed as a code.
Datatype: "PledgeeType1Code" on page 525
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 418 March 2026
```

