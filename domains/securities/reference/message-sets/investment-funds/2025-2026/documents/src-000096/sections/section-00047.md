---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["5 acmt.005.001.06 RequestForAccountManagementStatusReportV06", "5.2 Structure"]
file_pages: [78]
content_origin: "source-text-extraction"
mentioned_message_ids: ["acmt.005.001.06"]
---

# 5.2 Structure

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 78 to 78.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 78

```text
5.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <ReqForAcctMgmtStsRpt> [1..1]  
   MessageIdentification <MsgId> [1..1] ± 79
   RequestDetails <ReqDtls> [1..1]  C3 79
     LinkedReference <LkdRef> [0..1]  C4, C5 80
{Or       PreviousReference <PrvsRef> [1..1] ± 81
Or}       OtherReference <OthrRef> [1..1] ± 81
     StatusRequestType <StsReqTp> [1..1] CodeSet 81
     AccountApplicationIdentification <AcctApplId> [0..1] Text 82
     ExistingAccountIdentification <ExstgAcctId> [0..1] ± 82
     InvestmentAccount <InvstmtAcct> [0..1]  82
       AccountIdentification <AcctId> [1..1] Text 83
       AccountName <AcctNm> [0..1] Text 83
       AccountDesignation <AcctDsgnt> [0..1] Text 83
       OwnerIdentification <OwnrId> [0..1]  83
{Or         IndividualOwnerIdentification <IndvOwnrId> [1..1]  83
{Or           IdentificationNumber <IdNb> [1..1] ± 84
Or}           PersonName <PrsnNm> [1..1] ± 84
Or}         OrganisationOwnerIdentification <OrgOwnrId> [1..1] ± 84
       AccountServicer <AcctSvcr> [0..1] ± 84
5.3 Constraints
C1 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C2 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C3 LinkedReferenceOrAccountApplicationIdentificationRule
Either LinkedReference or AccountApplicationIdentification must be present.
Approved by the Securities SEG on 27 January 2026 acmt.005.001.06
RequestForAccountManagementStatusReportV06
Investment Funds - Maintenance 2025 - 2026 78 May 2026
```

