---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["12 seev.040.001.13 CorporateActionInstructionCancellationRequestV13", "12.4 Message Building Blocks", "12.4.4 AccountDetails <AcctDtls>", "12.4.4.3 AccountOwner <AcctOwnr>"]
file_pages: [729]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.040.001.13"]
---

# 12.4.4.3 AccountOwner <AcctOwnr>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 729 to 729.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 729

```text
Datatype: "Max140Text" on page 1249
12.4.4.3  AccountOwner <AcctOwnr>
Presence: [0..1]
Definition: Party that legally owns the account.
AccountOwner <AcctOwnr> contains one of the following elements (see
"PartyIdentification127Choice" on page 1037 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C1 1038
Or}   ProprietaryIdentification <PrtryId> [1..1] ± 1038
12.4.4.4  SafekeepingPlace <SfkpgPlc>
Presence: [0..1]
Definition: Location where the financial instruments are/will be safekept.
SafekeepingPlace <SfkpgPlc> contains one of the following elements (see
"SafekeepingPlaceFormat42Choice" on page 1130 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Identification <Id> [1..1]  1130
     SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 1130
     Identification <Id> [0..1] Text 1131
Or   Country <Ctry> [1..1] CodeSet C3 1131
Or   DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 1131
Or   TypeAndIdentification <TpAndId> [1..1]  1131
     SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 1132
     Identification <Id> [1..1] IdentifierSet C1 1132
Or}   Proprietary <Prtry> [1..1] ± 1132
12.4.5 CorporateActionInstruction <CorpActnInstr>
Presence: [1..1]
Definition: Information about the corporate action option.
Impacted by: C14 "OptionNumber1Rule", C15 "OptionNumber2Rule"
Approved by the Securities SEG on 27 January 2026 seev.040.001.13
CorporateActionInstructionCancellationRequestV13
Corporate Actions - Maintenance 2025 - 2026 729 February 2026
```

