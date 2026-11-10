---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.20 SolicitationAgent <SlctnAgt>"]
file_pages: [263, 264]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.20 SolicitationAgent <SlctnAgt>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 263 to 264.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 263

```text
PhysicalSecuritiesAgent <PhysSctiesAgt> contains one of the following elements (see
"PartyIdentification120Choice" on page 1045 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C1 1045
Or   ProprietaryIdentification <PrtryId> [1..1] ± 1046
Or}   NameAndAddress <NmAndAdr> [1..1] ± 1046
3.4.19 DropAgent <DrpAgt>
Presence: [0..1]
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
3.4.20 SolicitationAgent <SlctnAgt>
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
3.4.21 InformationAgent <InfAgt>
Presence: [0..1]
Definition: Trust company, bank or similar financial institution assigned by an Issuer to provide
information and copies of the offering documentation.
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 263 February 2026
```

## File page 264

```text
InformationAgent <InfAgt> contains one of the following elements (see "PartyIdentification120Choice"
on page 1045 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C1 1045
Or   ProprietaryIdentification <PrtryId> [1..1] ± 1046
Or}   NameAndAddress <NmAndAdr> [1..1] ± 1046
3.4.22 Issuer <Issr>
Presence: [0..1]
Definition: Issuer of the financial instrument.
Issuer <Issr> contains one of the following elements (see "PartyIdentification129Choice" on page 1042
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C1 1043
Or   ProprietaryIdentification <PrtryId> [1..1] ± 1043
Or   NameAndAddress <NmAndAdr> [1..1] ± 1043
Or}   LEI <LEI> [1..1] IdentifierSet 1043
3.4.23 Offeror <Offerr>
Presence: [0..*]
Definition: Party making the offer and which is different from the issuing company.
Offeror <Offerr> contains one of the following elements (see "PartyIdentification129Choice" on
page 1042 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C1 1043
Or   ProprietaryIdentification <PrtryId> [1..1] ± 1043
Or   NameAndAddress <NmAndAdr> [1..1] ± 1043
Or}   LEI <LEI> [1..1] IdentifierSet 1043
3.4.24 TransferAgent <TrfAgt>
Presence: [0..1]
Definition: Trust company, bank or similar financial institution appointed by a fund management
company to maintain records of investors and account balances. The transfer agent records
transactions, including subscriptions, redemptions, switches, transfers, and re-registrations.
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 264 February 2026
```

