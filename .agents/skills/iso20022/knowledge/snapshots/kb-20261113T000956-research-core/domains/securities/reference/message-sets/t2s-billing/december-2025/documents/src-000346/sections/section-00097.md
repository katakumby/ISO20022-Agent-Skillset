---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S Billing"
source_ids: ["src-000346"]
source_editions: ["december-2025"]
message_ids: []
heading_path: ["4 Message Items Types", "4.1 MessageComponents", "4.1.7 Party Identification", "4.1.7.2 PartyIdentification136"]
file_pages: [123]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 4.1.7.2 PartyIdentification136

Source: [src-000346](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart1_Target2Securities_Billing_v1.pdf`. Locator: one-based file pages 123 to 123.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 123

```text
NameAndAddress <NmAndAdr> contains the following elements (see "NameAndAddress5" on
page 141 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 141
   Address <Adr> [0..1] ± 142
4.1.7.2  PartyIdentification136
Definition: Identification of the party.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 123
   LEI <LEI> [0..1] IdentifierSet 123
4.1.7.2.1  Identification <Id>
Presence: [1..1]
Definition: Unique identification of the party.
Identification <Id> contains one of the following elements (see "PartyIdentification120Choice" on
page 122 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C2 122
Or   ProprietaryIdentification <PrtryId> [1..1] ± 122
Or}   NameAndAddress <NmAndAdr> [1..1] ± 122
4.1.7.2.2  LEI <LEI>
Presence: [0..1]
Definition: Legal entity identification as an alternate identification for a party.
Datatype: "LEIIdentifier" on page 150
4.1.7.3  PartyIdentification272
Definition: Specifies the identification of a person or an organisation.
Approved by the Securities SEG on 20 November 2025 and the Payments
SEG on 01 December 2025, under the lead of the Securities Standards
Evaluation Group (SEG).
Message Items Types
Target2-Securities - Billing 123 December 2025
```

