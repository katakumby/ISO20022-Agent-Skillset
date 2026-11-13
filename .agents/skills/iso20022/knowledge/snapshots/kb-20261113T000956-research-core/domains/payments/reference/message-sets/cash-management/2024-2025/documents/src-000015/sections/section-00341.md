---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["13 camt.014.001.05 ReturnMemberV05", "13.4 Message Building Blocks", "13.4.2 ReportOrError <RptOrErr>", "13.4.2.1 Report <Rpt>", "13.4.2.1.1 MemberIdentification <MmbId>"]
file_pages: [484]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.014.001.05"]
---

# 13.4.2.1.1 MemberIdentification <MmbId>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 484 to 484.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 484

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         PhoneNumber <PhneNb> [1..1] Text 493
         FaxNumber <FaxNb> [0..1] Text 493
         EmailAddress <EmailAdr> [0..1] Text 493
Or}     BusinessError <BizErr> [1..1] ± 493
13.4.2.1.1  MemberIdentification <MmbId>
Presence: [1..1]
Definition: Unique and unambiguous identification of a member within a system, assigned using the
member identification scheme of the system.
MemberIdentification <MmbId> contains one of the following MemberIdentification3Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   BICFI <BICFI> [1..1] IdentifierSet C2 484
Or   ClearingSystemMemberIdentification <ClrSysMmbId> [1..1] ± 484
Or}   Other <Othr> [1..1] ± 485
13.4.2.1.1.1  BICFI <BICFI>
Presence: [1..1]
Definition: Business identification code of the member financial institution.
Impacted by: C2 "BICFI"
Datatype: "BICFIDec2014Identifier" on page 884
Constraints
• BICFI
Valid BICs for financial institutions are registered and published by the ISO 9362 Registration
Authority in the ISO directory of BICs, and consist of eight (8) or eleven (11) contiguous characters.
13.4.2.1.1.2  ClearingSystemMemberIdentification <ClrSysMmbId>
Presence: [1..1]
Definition: Information used to identify a member within a clearing system.
ClearingSystemMemberIdentification <ClrSysMmbId> contains the following elements (see
"ClearingSystemMemberIdentification2" on page 802 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ClearingSystemIdentification <ClrSysId> [0..1] ± 802
   MemberIdentification <MmbId> [1..1] Text 802
Approved by the Payments SEG on 04 February 2025 camt.014.001.05 ReturnMemberV05
Cash Management - Maintenance 2024 - 2025 484 February 2025
```

