WITH matched_assignments AS (
  SELECT
    a.AgentID,
    a.FirstName,
    a.LastName,
    a.AverageCustomerServiceRating
  FROM assignment_history ah
  JOIN bookings b ON ah.AssignmentID = b.AssignmentID
  JOIN space_travel_agents a ON ah.AgentID = a.AgentID
  WHERE ah.CommunicationMethod = :CommunicationMethod
    AND ah.LeadSource = :LeadSource
    AND b.Destination = :Destination
    AND b.LaunchLocation = :LaunchLocation
)

SELECT
  FirstName,
  LastName,
  AverageCustomerServiceRating
FROM matched_assignments
GROUP BY AgentID
ORDER BY AverageCustomerServiceRating DESC;