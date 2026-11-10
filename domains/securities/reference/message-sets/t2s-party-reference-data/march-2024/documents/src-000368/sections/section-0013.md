---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S PartyReferenceData"
source_ids: ["src-000368"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Functionality"]
content_origin: "source-transcription"
---

# Functionality

Source: [src-000368](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_PartyReferenceData_2023_2024_v2.docx`. Locator: heading path Scope and Functionality / Groups of MessageDefinitions and Functionality / Functionality.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P91** Functionality

**P92** The Party Reference Data message definitions are specifically designed to support the following technical functions:

**P94** Party Creation Request (reda.014) provides a user, granted with the appropriate rights, with the possibility to create a new Party.  
  
The user has to specify information that clearly identifies the party, as for example BIC, opening and closing date, classification, long and short name.   
  
The Party Status Advice (reda.016) informs the Instructing Party about the lifecycle of its party creation request.

**P96** Party Modification Request (reda.022) provides a user, granted with the appropriate rights, with the possibility to update an active and valid party.  
  
The Instructing Party can also block or unblock the related Party.  
  
The Party Status Advice (reda.016) informs the Instructing Party about the lifecycle of the party modification request.  


**P97** Party Deletion Request (reda.031) provides a user, granted with the appropriate rights, with the possibility to delete an existing party.   
  
The Party Status Advice (reda.016) informs the Instructing Party about the lifecycle of the party deletion request.

**P99** Party Query (reda.015) is sent by an authorised party to query on party reference data.    
  
This message is sent to the servicing party to make the following type of queries:  
-   Party Reference Data Query;  
-   Party List Query;  
-   Restricted Party Query.   
  
Depending on the query criteria, it is possible that the processing will take more than a certain time or that the query will not retrieve any record. In this case, an error is sent to the Instructing Party within the Party Report message (reda.017).  
  
Search criteria include the following elements:   
- Party BIC;  
- Opening and closing date;  
- Type of the party;  
- Responsible CSD or CB;  
- Restriction.  


**P100** Party Report (reda.017) is sent to the Instructing Party and includes all of the party records that meet the specified criteria or reports any possible error (e.g. not allowed set of search criteria).   
  
This query response contains the timestamp specifying the system time when the data selection was actually performed.  
  
The Party Report is capable to report any piece of information related to a party, including BIC, name, address, technical address, restrictions and market specific attributes.

**P101** Party Activity Advice (reda.041) is sent to authorised recipients by the servicing party to provide with information on changes occurred during the business day on party reference data.  
  
The Party Activity Advice is capable to report any change applied to every piece of information for a party, including BIC, name, address, technical address, restrictions and market specific attributes.

**P102** Party Audit Trail Query (reda.042) is sent by an authorised party to query on audit trail for party reference data.   
  
Depending on the query criteria, it is possible that the processing will take more than a certain time or that the query will not retrieve any record. In this case, an error is sent to the Instructing Party within the Party Report message.  
  
Search criteria include the following elements:   
- Party;  
- Date Period.  


**P103** Party Audit Trail Report (reda.043) is sent to the Instructing Party and includes all of the party audit trail records that meet the specified criteria or reports any possible error (e.g. empty list retrieved).   
  
This query response contains the timestamp specifying the system time when the data selection was actually performed.  
  
The Party Audit Trail Report is capable to report any change applied to every piece of information for a party, including BIC, name, address, technical address, restrictions and market specific attributes along with the reference of the user performing the change and the related timestamp.

**P105** See Message Definition Report Part 2 for the message and formats.

