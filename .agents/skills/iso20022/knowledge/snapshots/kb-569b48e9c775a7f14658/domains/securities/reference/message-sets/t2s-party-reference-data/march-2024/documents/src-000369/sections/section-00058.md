---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S PartyReferenceData"
source_ids: ["src-000369"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["6 reda.022.001.02 PartyModificationRequestV02", "6.4 Message Building Blocks", "6.4.3 Modification <Mod>", "6.4.3.2 RequestedModification <ReqdMod>", "6.4.3.2.3 PartyName <PtyNm>"]
file_pages: [69]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.022.001.02"]
---

# 6.4.3.2.3 PartyName <PtyNm>

Source: [src-000369](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_PartyReferenceData_2023_2024_v1.pdf`. Locator: one-based file pages 69 to 69.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 69

```text
6.4.3.2.3  PartyName <PtyNm>
Presence: [1..1]
Definition: Specifies the name by which a party is known and which is usually used to identify that party.
PartyName <PtyNm> contains the following PartyName3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ValidFrom <VldFr> [0..1] Date 69
   Name <Nm> [0..1] Text 69
   ShortName <ShrtNm> [0..1] Text 69
6.4.3.2.3.1  ValidFrom <VldFr>
Presence: [0..1]
Definition: Specifies the date from which the party name is valid.
Datatype: "ISODate" on page 184
6.4.3.2.3.2  Name <Nm>
Presence: [0..1]
Definition: Name by which a party is known and which is usually used to identify that party.
Datatype: "Max350Text" on page 187
6.4.3.2.3.3  ShortName <ShrtNm>
Presence: [0..1]
Definition: Specifies the short name of the organisation.
Datatype: "Max35Text" on page 188
6.4.3.2.4  ContactDetails <CtctDtls>
Presence: [1..1]
Definition: Specifies the options on how to contact the party.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
reda.022.001.02 PartyModificationRequestV02
Target2-Securities - Party Reference Data - Maintenance
2023 - 2024
69 March 2024
```

