---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["5 seev.033.001.14 CorporateActionInstructionV14", "5.4 Message Building Blocks", "5.4.8 BeneficialOwnerDetails <BnfclOwnrDtls>", "5.4.8.1 OwnerIdentification <OwnrId>"]
file_pages: [301]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.033.001.14"]
---

# 5.4.8.1 OwnerIdentification <OwnrId>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 301 to 301.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 301

```text
BeneficialOwnerDetails <BnfclOwnrDtls> contains the following PartyIdentification340 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OwnerIdentification <OwnrId> [1..1] ± 301
   AlternateIdentification <AltrnId> [0..*] ± 301
   DomicileCountry <DmclCtry> [0..1] CodeSet C8 302
   NonDomicileCountry <NonDmclCtry> [0..*] CodeSet C8 302
   OwnedSecuritiesQuantity <OwndSctiesQty> [1..1] ± C12 302
   CertificationType <CertfctnTp> [0..*] ± 303
   WithholdingTaxRate <WhldgTaxRate> [0..1] ± 303
   CertificationBreakdown <CertfctnBrkdwn> [0..*] Text 303
5.4.8.1  OwnerIdentification <OwnrId>
Presence: [1..1]
Definition: Party that is the beneficial owner of the specified quantity of securities.
OwnerIdentification <OwnrId> contains one of the following elements (see
"PartyIdentification263Choice" on page 1048 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C1 1048
Or   ProprietaryIdentification <PrtryId> [1..1] ± 1049
Or   NameAndAddress <NmAndAdr> [1..1] ± 1049
Or   IndividualOwnerIdentification <IndvOwnrId> [1..1] ± 1049
Or}   LEI <LEI> [1..1] IdentifierSet 1050
5.4.8.2  AlternateIdentification <AltrnId>
Presence: [0..*]
Definition: Alternate identification for a party.
AlternateIdentification <AltrnId> contains the following elements (see "AlternatePartyIdentification12"
on page 1047 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   IdentificationType <IdTp> [1..1] ± 1047
   Country <Ctry> [1..1] CodeSet C3 1048
   AlternateIdentification <AltrnId> [1..1] Text 1048
   LEI <LEI> [0..1] IdentifierSet 1048
Approved by the Securities SEG on 27 January 2026 seev.033.001.14 CorporateActionInstructionV14
Corporate Actions - Maintenance 2025 - 2026 301 February 2026
```

