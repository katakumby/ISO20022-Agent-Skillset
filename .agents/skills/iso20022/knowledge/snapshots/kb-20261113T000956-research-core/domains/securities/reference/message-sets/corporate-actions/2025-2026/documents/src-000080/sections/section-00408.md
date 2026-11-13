---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["7 seev.035.001.17 CorporateActionMovementPreliminaryAdviceV17", "7.4 Message Building Blocks", "7.4.22 SolicitationAgent <SlctnAgt>"]
file_pages: [537]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.035.001.17"]
---

# 7.4.22 SolicitationAgent <SlctnAgt>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 537 to 537.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 537

```text
Definition: Trust company, bank or similar financial institution that acts on behalf of an out-of-town agent
or event agent where securities can be delivered in person.
DropAgent <DrpAgt> contains one of the following elements (see "PartyIdentification120Choice" on
page 1045 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C1 1045
Or   ProprietaryIdentification <PrtryId> [1..1] ± 1046
Or}   NameAndAddress <NmAndAdr> [1..1] ± 1046
7.4.22 SolicitationAgent <SlctnAgt>
Presence: [0..*]
Definition: Trust company, bank or similar financial institution assigned by an issuer to maintain records
of investors and account balances and transactions for the consent of a material change.
SolicitationAgent <SlctnAgt> contains one of the following elements (see
"PartyIdentification120Choice" on page 1045 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C1 1045
Or   ProprietaryIdentification <PrtryId> [1..1] ± 1046
Or}   NameAndAddress <NmAndAdr> [1..1] ± 1046
7.4.23 InformationAgent <InfAgt>
Presence: [0..1]
Definition: Trust company, bank or similar financial institution assigned by an Issuer to provide
information and copies of the offering documentation.
InformationAgent <InfAgt> contains one of the following elements (see "PartyIdentification120Choice"
on page 1045 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C1 1045
Or   ProprietaryIdentification <PrtryId> [1..1] ± 1046
Or}   NameAndAddress <NmAndAdr> [1..1] ± 1046
7.4.24 Issuer <Issr>
Presence: [0..1]
Definition: Issuer of the financial instrument.
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 537 February 2026
```

