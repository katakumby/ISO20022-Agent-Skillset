---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000377"]
source_editions: ["june-2021"]
message_ids: []
heading_path: ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Securities Reference Data message "]
content_origin: "source-transcription"
---

# Securities Reference Data message 

Source: [src-000377](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesReferenceData_v2.docx`. Locator: heading path Scope and Functionality / Groups of MessageDefinitions and Functionality / Groups / Securities Reference Data message .

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P92** Securities Reference Data message 

[T4 - complete table](../tables/tbl-0004.md)

**P93** The securities reference data messages are specifically designed to support the following functions:

**P95** Security Creation Request (reda.006) provides a user, granted with the appropriate rights, with the possibility to create a new Security.  
  
The user has to specify information that clearly identifies the Security, as for example ISIN, security long name, security short name, valid from name, denomination currency, classification type, issuance details, settlement information.  
  
The Security Creation Status Advice (reda.008) informs the Instructing Party about the lifecycle of its security creation request.

**P97** Security Maintenance Request (reda.007) provides a user, granted with the appropriate rights, with the possibility to update an active and valid security.  
  
The Security Maintenance Status Advice (reda.029) informs the Instructing Party about the lifecycle of its security modification request.

**P99** Security Deletion Request (reda.013) provides a user, granted with the appropriate rights, with the possibility to delete an existing security.  
  
The Security Deletion Status Advice (reda.030) informs the Instructing Party about the lifecycle of its security deletion request.

**P101** Security Query (reda.010) is sent by an authorised party to query on security reference data.  
  
This message is sent to the servicing party to make the following type of queries:

**P102** Securities Reference Data Query;

**P103** ISIN List Query;

**P104** Securities CSD Link Query;

**P105** Securities Deviating Nominal Query.

**P107** Depending on the query criteria, it is possible that the processing will take more than a certain time or that the query will not retrieve any record. In this case, an error is sent to the Instructing Party within the Security Report (reda.012);   
  
Search criteria include the following elements: 

**P108** ISIN;

**P109** Classification Type;

**P110** Maturity Date;

**P111** Issue Date;

**P112** Issue Currency;

**P113** Country of Issue;

**P114** Maintainer CSD; 

**P115** Investor CSD;

**P116** Issuer CSD;

**P117** Technical Issuer CSD;

**P118** Generic CSD of a security, both investor and issuer CSDs.

**P120** Security Report (reda.012) is sent to the Instructing Party and includes all of the Securities records that meet the specified criteria or reports any possible error (e.g. not allowed set of search criteria).  
  
This query response contains the timestamp specifying the system time when the data selection was actually performed.  
  
The Security Report is capable to report any piece of information related to a security, including ISIN, financial instrument name, denomination currency, expiry date, classification type, country of issuance, issue date, restriction, financial instrument identification validity, settlement information.

**P122** Security Activity Advice (reda.009) is sent to authorised recipients by the servicing party to provide with information on changes occurred during the business day on security reference data.  
  
Security Activity Advice is capable to report any change applied to every piece of information for a security, including financial instrument name, denomination currency, expiry date, classification type, country of issuance, issue date, restriction, financial instrument identification validity, settlement information.

**P124** Securities Audit Trail Query (reda.033) is sent by an authorised party to query on audit trail for securities reference data.  
  
Depending on the query criteria, it is possible that the processing will take more than a certain time or that the query will not retrieve any record. In this case, an error is sent to the Instructing Party within the Securities Audit Trail Report message (reda.034).  
  
Search criteria include the following elements: 

**P125** ISIN;

**P126** Date Period.

**P128** Securities Audit Trail Report (reda.034) is sent to the Instructing Party and includes all of the securities audit trail records that meet the specified criteria or reports any possible error (e.g. empty list retrieved).   
  
This query response contains the timestamp specifying the system time when the data selection was actually performed.  
  
Securities Audit Trail Report is capable to report any change applied to every piece of information for a security along with the reference of the user performing the change and the related timestamp.

