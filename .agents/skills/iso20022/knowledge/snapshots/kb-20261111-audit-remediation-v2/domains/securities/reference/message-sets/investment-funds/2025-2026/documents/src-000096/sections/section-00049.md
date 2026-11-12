---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["5 acmt.005.001.06 RequestForAccountManagementStatusReportV06", "5.4 Message Building Blocks", "5.4.2 RequestDetails <ReqDtls>", "5.4.2.1 LinkedReference <LkdRef>"]
file_pages: [80]
content_origin: "source-text-extraction"
mentioned_message_ids: ["acmt.005.001.06"]
---

# 5.4.2.1 LinkedReference <LkdRef>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 80 to 80.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 80

```text
RequestDetails <ReqDtls> contains the following AccountManagementMessageReference5
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   LinkedReference <LkdRef> [0..1]  C4, C5 80
{Or     PreviousReference <PrvsRef> [1..1] ± 81
Or}     OtherReference <OthrRef> [1..1] ± 81
   StatusRequestType <StsReqTp> [1..1] CodeSet 81
   AccountApplicationIdentification <AcctApplId> [0..1] Text 82
   ExistingAccountIdentification <ExstgAcctId> [0..1] ± 82
   InvestmentAccount <InvstmtAcct> [0..1]  82
     AccountIdentification <AcctId> [1..1] Text 83
     AccountName <AcctNm> [0..1] Text 83
     AccountDesignation <AcctDsgnt> [0..1] Text 83
     OwnerIdentification <OwnrId> [0..1]  83
{Or       IndividualOwnerIdentification <IndvOwnrId> [1..1]  83
{Or         IdentificationNumber <IdNb> [1..1] ± 84
Or}         PersonName <PrsnNm> [1..1] ± 84
Or}       OrganisationOwnerIdentification <OrgOwnrId> [1..1] ± 84
     AccountServicer <AcctSvcr> [0..1] ± 84
Constraints
• LinkedReferenceOrAccountApplicationIdentificationRule
Either LinkedReference or AccountApplicationIdentification must be present.
5.4.2.1  LinkedReference <LkdRef>
Presence: [0..1]
Definition: Reference to a linked message.
Impacted by: C4 "OtherReferenceGuideline", C5 "PreviousReferenceGuideline"
LinkedReference <LkdRef> contains one of the following LinkedMessage5Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   PreviousReference <PrvsRef> [1..1] ± 81
Or}   OtherReference <OthrRef> [1..1] ± 81
Approved by the Securities SEG on 27 January 2026 acmt.005.001.06
RequestForAccountManagementStatusReportV06
Investment Funds - Maintenance 2025 - 2026 80 May 2026
```

