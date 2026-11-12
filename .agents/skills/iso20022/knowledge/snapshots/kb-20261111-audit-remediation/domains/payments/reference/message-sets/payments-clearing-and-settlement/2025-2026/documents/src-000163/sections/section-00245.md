---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pacs.004.001.15 PaymentReturnV15", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.3.26 ReturnReasonInformation <RtrRsnInf>"]
file_pages: [348]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.004.001.15"]
---

# 4.4.3.26 ReturnReasonInformation <RtrRsnInf>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 348 to 348.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 348

```text
Agent <Agt> contains the following elements (see "BranchAndFinancialInstitutionIdentification8" on
page 1173 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstitutionIdentification <FinInstnId> [1..1]  1174
     BICFI <BICFI> [0..1] IdentifierSet C5 1174
     ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 1175
     LEI <LEI> [0..1] IdentifierSet 1175
     Name <Nm> [0..1] Text 1175
     PostalAddress <PstlAdr> [0..1] ± 1175
     Other <Othr> [0..1] ± 1176
   BranchIdentification <BrnchId> [0..1]  1177
     Identification <Id> [0..1] Text 1177
     LEI <LEI> [0..1] IdentifierSet 1177
     Name <Nm> [0..1] Text 1177
     PostalAddress <PstlAdr> [0..1] ± 1177
4.4.3.26  ReturnReasonInformation <RtrRsnInf>
Presence: [0..*]
Definition: Provides detailed information on the return reason.
Impacted by: C62 "ReturnReasonRule"
ReturnReasonInformation <RtrRsnInf> contains the following PaymentReturnReason7 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Originator <Orgtr> [0..1] ± 349
   Reason <Rsn> [0..1]  350
{Or     Code <Cd> [1..1] CodeSet 350
Or}     Proprietary <Prtry> [1..1] Text 350
   AdditionalInformation <AddtlInf> [0..*] Text 350
Constraints
• ReturnReasonRule
If Reason/Code is equal to NARR, then AddititionalInformation must be present.
On Condition
    /Reason/Code is present
 And    /Reason/Code is within DataType <<Code>> ValidationRuleNarrative1Code
 And    /Reason is present
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
348 March 2026
```

