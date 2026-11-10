---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S LimitUtilisationJournal"
source_ids: ["src-000362"]
source_editions: ["february-2025"]
message_ids: []
heading_path: ["Scope and Functionality", "Scope", "Functionality"]
content_origin: "source-transcription"
---

# Functionality

Source: [src-000362](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LimitUtilisationJournal_MessageSet/ISO20022_MDRPart1_Target2Securities_LimitUtilisationJournal_v2.docx`. Locator: heading path Scope and Functionality / Scope / Functionality.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P58** Functionality

**P59** The Limit Utilisation Journal Query Report message definitions are specifically designed to support the following technical functions:

**P60** Limit Utilisation Journal Query

**P62** A CSD, NCB, payment bank or a directly connected system participant (the central securities depository participant granted direct access, like a bank or a central counterparty) sends the Limit Utilisation Journal Query message (camt.064) to T2S. It is used to request information regarding the journaling of cash limits utilisation (including limit amounts, utilisation and journal of transactions impacting the utilisation of limits) as managed by the credit provider and corresponding to the criteria as defined within the message as the following:

**P63** Mandatory business attributes include:

**P64** Party identification (party as credit consumer)

**P65** Responsible party identification (NCB acting as parent and as credit provider or CSD acting as parent of the client)

**P66** Date (journal activity date)

**P67** Optional business attributes include:

**P68** Dedicated cash account

**P69** Limit type:

**P70** Auto Collateralisation

**P71** External Guarantee

**P72** Unsecured Credit

**P73** In response to the Limit Utilisation Journal Query T2S sends a Limit Utilisation Journal Report message (camt.065) with the corresponding limit amounts, utilisations and journal activity matching the criteria as defined within the query.

**P75** Limit Utilisation Journal Report

**P77** The Limit Utilisation Journal Report message (camt.065) is sent by T2S to CSD, NCB, payment bank or a directly connected system participant (the central securities depository participant granted direct access, like a bank or a central counterparty). It is used to report information regarding the limits (including limit amounts, utilisation and journal of transactions impacting the utilisation of limits) as managed by the credit provider and corresponding to the criteria received within the incoming query message (camt.064).  


**P78** It includes the following business attributes as output parameters:

**P79** Party identification

**P80** Responsible party identification

**P81** Date

**P82** Dedicated cash account

**P83** Limit type

**P84** Debit/Credit indicator

**P85** Limit currency

**P86** Amount (initial amount of the limit)

**P87** Utilisation amount (utilised amount of the limit)

**P88** Available amount (remaining available headroom of the limit)

**P89** Transaction reference

**P90** See Message Definition Report Part 2 for the message and formats.

