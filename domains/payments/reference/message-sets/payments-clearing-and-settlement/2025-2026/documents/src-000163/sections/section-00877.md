---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["10 Message Items Types", "10.1 MessageComponents", "10.1.7 Financial Institution Identification"]
file_pages: [1172]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 10.1.7 Financial Institution Identification

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 1172 to 1172.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1172

```text
10.1.7 Financial Institution Identification
10.1.7.1  ClearingSystemMemberIdentification2
Definition: Unique identification, as assigned by a clearing system, to unambiguously identify a member
of the clearing system.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ClearingSystemIdentification <ClrSysId> [0..1] ± 1172
   MemberIdentification <MmbId> [1..1] Text 1172
10.1.7.1.1  ClearingSystemIdentification <ClrSysId>
Presence: [0..1]
Definition: Specification of a pre-agreed offering between clearing agents or the channel through which
the payment instruction is processed.
ClearingSystemIdentification <ClrSysId> contains one of the following elements (see
"ClearingSystemIdentification2Choice" on page 1220 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1220
Or}   Proprietary <Prtry> [1..1] Text 1220
10.1.7.1.2  MemberIdentification <MmbId>
Presence: [1..1]
Definition: Identification of a member of a clearing system.
Datatype: "Max35Text" on page 1246
10.1.7.2  GenericFinancialIdentification1
Definition: Information related to an identification of a financial institution.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1172
   SchemeName <SchmeNm> [0..1]  1173
{Or     Code <Cd> [1..1] CodeSet 1173
Or}     Proprietary <Prtry> [1..1] Text 1173
   Issuer <Issr> [0..1] Text 1173
10.1.7.2.1  Identification <Id>
Presence: [1..1]
Definition: Unique and unambiguous identification of a person.
Approved by the Payments SEG on 12 January 2026 Message Items Types
Payments Clearing and Settlement - Maintenance 2025 -
2026
1172 March 2026
```

