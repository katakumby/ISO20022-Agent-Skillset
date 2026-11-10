---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S Billing"
source_ids: ["src-000346"]
source_editions: ["december-2025"]
message_ids: []
heading_path: ["4 Message Items Types", "4.1 MessageComponents", "4.1.7 Party Identification", "4.1.7.3 PartyIdentification272", "4.1.7.3.3 Identification <Id>", "4.1.7.3.3.1 OrganisationIdentification <OrgId>", "4.1.7.3.3.1.3 Other <Othr>", "4.1.7.3.3.1.3.1 Identification <Id>"]
file_pages: [128]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 4.1.7.3.3.1.3.1 Identification <Id>

Source: [src-000346](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart1_Target2Securities_Billing_v1.pdf`. Locator: one-based file pages 128 to 128.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 128

```text
Other <Othr> contains the following GenericOrganisationIdentification3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 128
   SchemeName <SchmeNm> [0..1]  128
{Or     Code <Cd> [1..1] CodeSet 128
Or}     Proprietary <Prtry> [1..1] Text 128
   Issuer <Issr> [0..1] Text 128
4.1.7.3.3.1.3.1  Identification <Id>
Presence: [1..1]
Definition: Identification assigned by an institution.
Datatype: "Max256Text" on page 152
4.1.7.3.3.1.3.2  SchemeName <SchmeNm>
Presence: [0..1]
Definition: Name of the identification scheme.
SchemeName <SchmeNm> contains one of the following
OrganisationIdentificationSchemeName1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 128
Or}   Proprietary <Prtry> [1..1] Text 128
4.1.7.3.3.1.3.2.1  Code <Cd>
Presence: [1..1]
Definition: Name of the identification scheme, in a coded form as published in an external list.
Datatype: "ExternalOrganisationIdentification1Code" on page 146
4.1.7.3.3.1.3.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Name of the identification scheme, in a free text form.
Datatype: "Max35Text" on page 153
4.1.7.3.3.1.3.3  Issuer <Issr>
Presence: [0..1]
Definition: Entity that assigns the identification.
Datatype: "Max35Text" on page 153
4.1.7.3.3.2  PrivateIdentification <PrvtId>
Presence: [1..1]
Approved by the Securities SEG on 20 November 2025 and the Payments
SEG on 01 December 2025, under the lead of the Securities Standards
Evaluation Group (SEG).
Message Items Types
Target2-Securities - Billing 128 December 2025
```

