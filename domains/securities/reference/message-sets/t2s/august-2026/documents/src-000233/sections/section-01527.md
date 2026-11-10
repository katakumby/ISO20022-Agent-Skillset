---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["42 reda.022.001.02 PartyModificationRequestV02", "42.4 Message Building Blocks", "42.4.3 Modification <Mod>", "42.4.3.2 RequestedModification <ReqdMod>", "42.4.3.2.3 PartyName <PtyNm>"]
file_pages: [2148]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.022.001.02"]
---

# 42.4.3.2.3 PartyName <PtyNm>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2148 to 2148.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2148

```text
42.4.3.2.3  PartyName <PtyNm>
Presence: [1..1]
Definition: Specifies the name by which a party is known and which is usually used to identify that party.
PartyName <PtyNm> contains the following PartyName3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ValidFrom <VldFr> [0..1] Date 2148
   Name <Nm> [0..1] Text 2148
   ShortName <ShrtNm> [0..1] Text 2148
42.4.3.2.3.1  ValidFrom <VldFr>
Presence: [0..1]
Definition: Specifies the date from which the party name is valid.
Datatype: "ISODate" on page 3319
42.4.3.2.3.2  Name <Nm>
Presence: [0..1]
Definition: Name by which a party is known and which is usually used to identify that party.
Datatype: "Max350Text" on page 3328
42.4.3.2.3.3  ShortName <ShrtNm>
Presence: [0..1]
Definition: Specifies the short name of the organisation.
Datatype: "Max35Text" on page 3328
42.4.3.2.4  ContactDetails <CtctDtls>
Presence: [1..1]
Definition: Specifies the options on how to contact the party.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.022.001.02 PartyModificationRequestV02
Target2-Securities 2148 August 2026
```

